import logging
from typing import List

from botocore.exceptions import ClientError
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from config import BUCKET_NAME, ALLOWED_FILE_EXTENSIONS, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from database import get_async_session
import boto3
from boto3.s3.transfer import TransferConfig
from auth.models import User
from videos.models import Video, Reaction, ReactionType, Comment
from auth.base_config import current_user
from videos.shemas import VideoRead, ReactionRead, CommentRead

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


# TODO(codEnjoyer): Предлагаю заменить preview_file: UploadFile = File() на preview_file: UploadFile | None = None
# а user: User = Depends(current_user) на user: Annotated[User, Depends(current_user)]
@router.post("/upload")
async def upload(video_file: UploadFile = File(),
                 preview_file: UploadFile = File(),
                 user: User = Depends(current_user),
                 async_session: AsyncSession = Depends(get_async_session)) -> VideoRead:
    if not any(video_file.filename.endswith(ext) for ext in ALLOWED_FILE_EXTENSIONS):
        raise HTTPException(status_code=400, detail="Invalid file type")
    if video_file.size > MAX_VIDEO_SIZE:
        raise HTTPException(status_code=400, detail=f"Invalid file size - {video_file.size / 1024 / 1024} mb")
    filename = video_file.filename.rsplit('.', 1)[0]
    s3.upload_fileobj(video_file.file, BUCKET_NAME, f"{user.id}/{filename}/video", Config=transfer_config)
    s3.upload_fileobj(preview_file.file, BUCKET_NAME, f"{user.id}/{filename}/preview", Config=transfer_config)
    return await upload_video_db(async_session, filename, user.id)


@router.post("/reaction")
async def post_reaction(video_id: int,
                        reaction_type: ReactionType,
                        user: User = Depends(current_user),
                        async_session: AsyncSession = Depends(get_async_session)) -> ReactionRead:
    reaction = await async_session.scalar(
        select(Reaction).where((user.id == Reaction.user_id) & (video_id == Reaction.video_id)))
    video = await get_user_video_model_with_id(async_session, video_id)
    if reaction:
        video.count_reactions -= 1
        await async_session.delete(reaction)
    else:
        reaction = Reaction(video_id=video_id, user_id=user.id, reaction_type_id=int(reaction_type))
        video.count_reactions += 1
        async_session.add(reaction)
    stmt = (update(Video).where(Video.id == video.id).values(count_reactions=video.count_reactions))
    await async_session.execute(stmt)
    await async_session.commit()
    return ReactionRead(user_id=user.id, video_id=video_id, reaction_type=int(reaction_type))


@router.post("/post_comment")
async def post_comment(video_id: int, text: str,
                       user: User = Depends(current_user),
                       async_session: AsyncSession = Depends(get_async_session)) -> CommentRead:
    comment = Comment(user_id=user.id, video_id=video_id, text=text)
    async_session.add(comment)
    await async_session.commit()
    return get_comment_info(comment)


@router.get('/comments')
async def get_comments_by_video_id(video_id: int, count: int = 5, offset: int = 0,
                                   db_session: AsyncSession = Depends(get_async_session)) -> List[CommentRead]:
    comments = await db_session.scalars(
        select(Comment).where(Comment.video_id == video_id).offset(offset).limit(count))
    return get_comments_info(comments)

@router.get("/get_my_videos")
async def get_my_videos(count: int = 5,
                        user: User = Depends(current_user),
                        async_session: AsyncSession = Depends(get_async_session)) -> List[VideoRead]:
    videos = await get_user_video_models(async_session, user.id, count)
    return await get_videos_info(videos)


@router.get("/get_videos")
async def get_videos(user_id: int, count: int = 5,
                     async_session: AsyncSession = Depends(get_async_session)) -> List[VideoRead]:
    videos = await get_user_video_models(async_session, user_id, count)
    return await get_videos_info(videos)


@router.get("/reaction_videos")
async def get_reaction_videos(count: int, offset: int,
                              reaction_type: ReactionType,
                              user: User = Depends(current_user),
                              async_session: AsyncSession = Depends(get_async_session)) -> List[VideoRead]:
    liked_videos = await async_session.scalars(
        select(Video)
        .join(Reaction)
        .where((Reaction.user_id == user.id) & (Reaction.reaction_type_id == int(reaction_type)))
        .offset(offset).limit(count))
    return await get_videos_info(liked_videos)


@router.delete("/delete/{video_id}")
async def delete_video(video_id: int,
                       user: User = Depends(current_user),
                       async_session: AsyncSession = Depends(get_async_session)) -> VideoRead:
    video = await get_user_video_model_with_id(async_session, video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    if video.user_id != user.id:
        raise HTTPException(status_code=403, detail="Access denied")
    await async_session.delete(video)
    await async_session.commit()
    s3.delete_object(Bucket=BUCKET_NAME, Key=f"{user.id}/{video.name}")
    return await get_video_info(video)


async def get_user_video_model_with_id(async_session: AsyncSession, video_id: int):
    try:
        stmt = select(Video).filter(Video.id == video_id)
        video = await async_session.scalar(stmt)
        return video
    except Exception as e:
        await async_session.rollback()
        raise e
    finally:
        await async_session.close()


async def get_user_video_models(async_session: AsyncSession, user_id: int, count: int = 5):
    try:
        stmt = select(Video).filter(Video.user_id == user_id).limit(count)
        if count == 1:
            videos = await async_session.scalar(stmt)
        else:
            videos = await async_session.scalars(stmt)
        if videos is None:
            videos = []
        return videos
    except Exception as e:
        await async_session.rollback()
        raise e
    finally:
        await async_session.close()


async def get_videos_info(videos) -> List[VideoRead]:
    videos_info = []
    for video in videos:
        video_info = await get_video_info(video)
        videos_info.append(video_info)
    return videos_info


async def get_video_info(video) -> VideoRead:
    video_url = await get_presigned_url(video.video_url)
    preview_url = await get_presigned_url(video.preview_url)
    return VideoRead(video_id=video.id,
                     name=video.name,
                     username=video.user.username,
                     video_url=video_url,
                     preview_url=preview_url,
                     count_reactions=video.count_reactions,
                     upload_at=video.uploaded_at)


def get_comments_info(comments) -> List[CommentRead]:
    comments_read = []
    for comment in comments:
        comments_read.append(get_comment_info(comment))
    return comments_read


def get_comment_info(comment) -> CommentRead:
    return CommentRead(user_id=comment.user_id,
                       video_id=comment.video_id,
                       text=comment.text,
                       create_at=comment.create_at)


async def upload_video_db(async_session: AsyncSession, filename: str, user_id: int) -> VideoRead:
    try:
        video = Video(
            name=filename,
            video_url=f"{user_id}/{filename}/video",
            preview_url=f"{user_id}/{filename}/preview",
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
