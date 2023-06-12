import logging
from botocore.exceptions import ClientError
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import BUCKET_NAME, ALLOWED_FILE_EXTENSIONS, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from database import get_async_session
import boto3
from boto3.s3.transfer import TransferConfig
from auth.models import User
from videos.models import Video
from auth.base_config import current_user

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
    prefix="/videos",
    tags=["Video"]
)


async def get_presigned_url(video_name: str):
    """
    Generate a presigned URL to share an S3 object
    :param video_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    try:
        response = s3.generate_presigned_url('get_object',
                                             Params={'Bucket': BUCKET_NAME,
                                                     'Key': video_name})
    except ClientError as e:
        logging.error(e)
        return None

    return response


@router.post("/upload")
async def upload(video_file: UploadFile = File(),
                 preview_file: UploadFile = File(),
                 user: User = Depends(current_user),
                 async_session: AsyncSession = Depends(get_async_session)):
    if not any(video_file.filename.endswith(ext) for ext in ALLOWED_FILE_EXTENSIONS):
        raise HTTPException(status_code=400, detail="Invalid file type")
    if video_file.size > MAX_VIDEO_SIZE:
        raise HTTPException(status_code=400, detail=f"Invalid file size - {video_file.size / 1024 / 1024} mb")
    filename = video_file.filename.rsplit('.', 1)[0]
    s3.upload_fileobj(video_file.file, BUCKET_NAME, f"{user.id}/{filename}/video", Config=transfer_config)
    s3.upload_fileobj(preview_file.file, BUCKET_NAME, f"{user.id}/{filename}/preview", Config=transfer_config)
    await upload_video_db(async_session, filename, user.id)
    url = await get_presigned_url(filename)
    return {"url": url}


@router.get("/get_my_videos")
async def get_my_videos(count: int = 5,
                        user: User = Depends(current_user),
                        async_session: AsyncSession = Depends(get_async_session)):
    urls = []
    videos = await get_user_video_models(async_session, user.id, count)
    for video in videos:
        urls.append(await get_presigned_url(f"{user.id}/{video.name}/video"))
    return urls


@router.get("/get_videos")
async def get_videos(user_id: int, count: int = 5,
                    async_session: AsyncSession = Depends(get_async_session)):
    urls = []
    videos = await get_user_video_models(async_session, user_id, count)
    for video in videos:
        urls.append(await get_presigned_url(f"{user_id}/{video.name}/video"))
    return urls


@router.delete("/delete/{video_id}")
async def delete_video(video_id: int, 
                       user: User = Depends(current_user),
                       async_session: AsyncSession = Depends(get_async_session)):
    video = await get_user_video_model_with_id(async_session, video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    if video.user_id != user.id:
        raise HTTPException(status_code=403, detail="Access denied")
    await async_session.delete(video)
    await async_session.commit()
    s3.delete_object(Bucket=BUCKET_NAME, Key=f"{user.id}/{video.name}")
    return video
    

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


async def get_user_video_models(async_session: AsyncSession, user_id: int, count: int = 5,):
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


async def upload_video_db(async_session: AsyncSession, filename: str, user_id: int):
    try:
        video = Video(
            name=filename,
            video_url=f"{user_id}/{filename}/video",
            preview_url=f"{user_id}/{filename}/preview",
            user_id=user_id
        )
        async_session.add(video)
        await async_session.commit()
    except Exception as e:
        await async_session.rollback()
        raise e
    finally:
        await async_session.close()

