import logging
from typing import List, Annotated
import boto3
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import func
from io import BytesIO

from config import BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, ALLOWED_FILE_EXTENSIONS
from database import get_async_session
from auth.models import User
from videos.models import Video, Reaction, ReactionType, Comment, VideoSortType
from auth.base_config import current_user
from videos.sсhemas import VideoRead, ReactionRead, CommentRead

MAX_VIDEO_SIZE = 1024 * 1024 * 512  # = 512MB
CHUNK_SIZE = 1024 * 1024
transfer_config = TransferConfig(multipart_chunksize=CHUNK_SIZE)

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

router = APIRouter(
    prefix="/video",
    tags=["Video"]
)


async def get_presigned_url(file_name: str):
    try:
        response = s3.generate_presigned_url('get_object',
                                             Params={'Bucket': BUCKET_NAME,
                                                     'Key': file_name})
    except ClientError as e:
        logging.error(e)
        return None

    return response


@router.post("/upload")
async def upload(name: str, description: str = None,
                 video_file: UploadFile = File(),
                 preview_file: UploadFile | None = None,
                 user: User = Depends(current_user),
                 async_session: AsyncSession = Depends(get_async_session)):
    if video_file.size > MAX_VIDEO_SIZE:
        raise HTTPException(status_code=400, detail=f"Invalid file size - {video_file.size / 1024 / 1024} mb")
    video_extension = video_file.filename.split(".")[-1]
    s3.upload_fileobj(video_file.file, BUCKET_NAME, f"{user.id}/{name}/video.{video_extension}", Config=transfer_config)
    preview_extension = None
    if preview_file is not None:
        preview_extension = preview_file.filename.split(".")[-1]
        s3.upload_fileobj(preview_file.file, BUCKET_NAME, f"{user.id}/{name}/preview.{preview_extension}",
                          Config=transfer_config)

    return await upload_video_db(async_session, user.id, name,
                                 description, preview_file is not None,
                                 video_extension, preview_extension)


@router.post("/{video_id}/reaction")
async def post_reaction(video_id: int, reaction_type: ReactionType,
                        user: User = Depends(current_user),
                        async_session: AsyncSession = Depends(get_async_session)) -> ReactionRead:
    reaction = await async_session.scalar(
        select(Reaction).where((user.id == Reaction.user_id) & (video_id == Reaction.video_id)))
    video = await get_video_with_id(async_session, video_id)
    if reaction:
        video.add_reaction(ReactionType(reaction.reaction_type_id), -1)
        await async_session.delete(reaction)
    if not reaction or reaction.reaction_type_id != int(reaction_type):
        reaction = Reaction(video_id=video_id, user_id=user.id, reaction_type_id=int(reaction_type))
        video.add_reaction(reaction_type, 1)
        async_session.add(reaction)
    stmt = update(Video).where(Video.id == video.id).values(count_reactions=video.count_reactions,
                                                            count_likes=video.count_likes,
                                                            count_dislikes=video.count_dislikes,
                                                            )
    await async_session.execute(stmt)
    await async_session.commit()
    return ReactionRead(user_id=user.id, video_id=video_id, reaction_type=int(reaction_type))


@router.post("/{video_id}/comment/")
async def post_comment(video_id: int, text: str,
                       user: User = Depends(current_user),
                       async_session: AsyncSession = Depends(get_async_session)) -> CommentRead:
    comment = Comment(user_id=user.id, video_id=video_id, text=text)
    async_session.add(comment)
    await async_session.commit()
    return get_comment_info(comment)


@router.get('/search')
async def get_video_by_name(name: str, offset: int = 0, limit: int = 15,
                            async_session: AsyncSession = Depends(get_async_session)) -> List[VideoRead]:
    levenshtein_distance = len(name) // 3
    stmt = (select(Video)
            .filter((func.levenshtein(Video.name, name) <= levenshtein_distance) | (Video.name.ilike(f"%{name}%")))
            .offset(offset)
            .limit(limit))
    result = await async_session.execute(stmt)
    videos = result.scalars().all()
    return await get_videos_info(videos)


@router.get('/{video_id}')
async def get_video(video_id: int,
                    async_session: AsyncSession = Depends(get_async_session)) -> VideoRead:
    video = await get_video_with_id(async_session, video_id)
    reaction = await async_session.scalar(
        select(Reaction).where((Reaction.user_id == video.user_id) & (Reaction.video_id == video.id)))
    reaction_type_id = -1
    if reaction is not None:
        reaction_type_id = reaction.reaction_type_id
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return await get_video_info(video, reaction_type_id)


@router.get('/auth/{video_id}')
async def auth_get_video(video_id: int,
                         user: User = Depends(current_user),
                         async_session: AsyncSession = Depends(get_async_session)) -> VideoRead:
    video = await get_video_with_id(async_session, video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    reaction = await async_session.scalar(
        select(Reaction).where((Reaction.user_id == user.id) & (Reaction.video_id == video.id)))
    reaction_type_id = -1
    if reaction is not None:
        reaction_type_id = reaction.reaction_type_id
    stmt = update(Video).where(Video.id == video_id).values(count_views=video.count_views + 1)
    await async_session.execute(stmt)
    await async_session.commit()
    return await get_video_info(video, reaction_type_id)


@router.get('/{video_id}/comments')
async def get_comments(video_id: int, count: int = 5, offset: int = 0,
                       async_session: AsyncSession = Depends(get_async_session)) -> List[CommentRead]:
    comments = await async_session.scalars(
        select(Comment).where(Comment.video_id == video_id).offset(offset).limit(count))
    return get_comments_info(comments)


@router.get("/user/my")
async def get_my_videos(limit: int = 5, offset: int = 0,
                        user: User = Depends(current_user),
                        async_session: AsyncSession = Depends(get_async_session)) -> List[VideoRead]:
    videos = await get_user_video_models(async_session, user.id, offset, limit)
    return await get_videos_info(videos)


@router.get("/user/{user_id}")
async def get_videos(user_id: int, limit: int = 5, offset: int = 0,
                     async_session: AsyncSession = Depends(get_async_session)) -> List[VideoRead]:
    videos = await get_user_video_models(async_session, user_id, offset, limit)
    return await get_videos_info(videos)


@router.get("/reacted")
async def get_reaction_videos(offset: int = 0,
                              limit: int = 15,
                              reaction_type: ReactionType = ReactionType.like,
                              user: User = Depends(current_user),
                              async_session: AsyncSession = Depends(get_async_session)) -> List[VideoRead]:
    liked_videos = await async_session.scalars(
        select(Video)
        .join(Reaction)
        .where((Reaction.user_id == user.id) & (Reaction.reaction_type_id == int(reaction_type)))
        .offset(offset).limit(limit))
    return await get_videos_info(liked_videos)


@router.delete("/remove/{video_id}")
async def delete_video(video_id: int,
                       user: User = Depends(current_user),
                       async_session: AsyncSession = Depends(get_async_session)) -> VideoRead:
    video = await get_video_with_id(async_session, video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    if video.user_id != user.id:
        raise HTTPException(status_code=403, detail="Access denied")
    await async_session.delete(video)
    await async_session.commit()
    s3.delete_object(Bucket=BUCKET_NAME, Key=f"{user.id}/{video.name}")
    return await get_video_info(video)


@router.delete("/{video_id}/comment/{comment_id}")
async def delete_comment(video_id: int, comment_id: int,
                         user: User = Depends(current_user),
                         async_session: AsyncSession = Depends(get_async_session)) -> CommentRead:
    video = await get_video_with_id(async_session, video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    comment = await async_session.scalar(select(Comment).where(Comment.id == comment_id))
    if comment.user_id != user.id:
        raise HTTPException(status_code=403, detail="Access denied")
    await async_session.delete(comment)
    await async_session.commit()
    return get_comment_info(comment)


async def get_video_with_id(async_session: AsyncSession, video_id: int) -> Video:
    stmt = select(Video).filter(Video.id == video_id)
    video = await async_session.scalar(stmt)
    return video


async def get_user_video_models(async_session: AsyncSession, user_id: int,
                                offset: int = 0, limit: int = 15) -> List[Video]:
    stmt = select(Video).filter(Video.user_id == user_id).offset(offset).limit(limit)
    videos = await async_session.scalars(stmt)
    if videos is None:
        videos = []
    return videos


async def get_last_video_models(async_session: AsyncSession, offset: int = 0, limit: int = 15):
    return await get_video_models(async_session, offset, limit, VideoSortType.count_likes)


async def get_video_models(async_session: AsyncSession, offset: int = 0, limit: int = 15,
                           sort_parameter: VideoSortType = VideoSortType.count_reactions):
    reactions = get_sort_parameter(sort_parameter)
    upload_time = get_sort_parameter(VideoSortType.upload_at)
    stmt = (select(Video)
            .order_by(reactions.desc())
            .order_by(upload_time.desc())
            .offset(offset)
            .limit(limit))
    videos = await async_session.scalars(stmt)
    return await get_videos_info(videos)


def get_sort_parameter(sort_parameter: VideoSortType):
    if sort_parameter == VideoSortType.count_reactions:
        return Video.count_reactions
    elif sort_parameter == VideoSortType.count_likes:
        return Video.count_likes
    elif sort_parameter == VideoSortType.count_dislikes:
        return Video.count_dislikes
    elif sort_parameter == VideoSortType.count_views:
        return Video.count_views
    elif sort_parameter == VideoSortType.upload_at:
        return Video.uploaded_at


async def get_videos_info(videos: List[Video]) -> List[VideoRead]:
    videos_info = []
    for video in videos:
        video_info = await get_video_info(video)
        videos_info.append(video_info)
    return videos_info


async def get_video_info(video: Video, reaction_type_id: int = -1) -> VideoRead:
    video_url = await get_presigned_url(video.video_url)
    preview_url = None
    if video.preview_url != "":
        preview_url = await get_presigned_url(video.preview_url)
    return VideoRead(video_id=video.id,
                     name=video.name,
                     description=video.description,
                     username=video.user.username,
                     video_url=video_url,
                     preview_url=preview_url,
                     reaction_type_id=reaction_type_id,
                     count_views=video.count_views,
                     count_reactions=video.count_reactions,
                     count_likes=video.count_likes,
                     count_dislikes=video.count_dislikes,
                     upload_at=video.uploaded_at,
                     user_id=video.user_id)


def get_comments_info(comments: List[Comment]) -> List[CommentRead]:
    comments_read = []
    for comment in comments:
        comments_read.append(get_comment_info(comment))
    return comments_read


def get_comment_info(comment: Comment) -> CommentRead:
    return CommentRead(user_id=comment.user_id,
                       video_id=comment.video_id,
                       text=comment.text,
                       create_at=comment.create_at,
                       username=comment.user.username)


async def upload_video_db(async_session: AsyncSession, user_id: int,
                          name: str, description: str, is_have_preview: bool,
                          video_ext: str, preview_ext: str) -> VideoRead:
    try:
        video = Video(
            name=name,
            description=description if description is not None else "",
            video_url=f"{user_id}/{name}/video.{video_ext}",
            preview_url=f"{user_id}/{name}/preview.{preview_ext}" if is_have_preview else "",
            user_id=user_id
        )
        async_session.add(video)
        await async_session.commit()
        return await get_video_info(video)
    except Exception as e:
        await async_session.rollback()
        raise e
    finally:
        await async_session.close()
