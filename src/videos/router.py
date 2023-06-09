import logging
from botocore.exceptions import ClientError
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config import BUCKET_NAME, ALLOWED_FILE_EXTENSIONS
from database import engine
import boto3
from auth.models import User
from auth.manager import get_user_by_id
from videos.models import Video
from auth.base_config import current_user

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

router = APIRouter(
    prefix="/videos",
    tags=["Video"]
)


async def get_presigned_url(video_name: str):
    """Generate a presigned URL to share an S3 object

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


@router.post("/post_video")
async def post_video(video_file: UploadFile = File(),
                     preview_file: UploadFile = File(),
                     user: User = Depends(current_user)):
    if not any(video_file.filename.endswith(ext) for ext in ALLOWED_FILE_EXTENSIONS):
        raise HTTPException(status_code=400, detail="Invalid file type")
    filename = video_file.filename.rsplit('.', 1)[0]
    s3.upload_fileobj(video_file.file, BUCKET_NAME, f"{user.id}/{filename}/video")
    s3.upload_fileobj(preview_file.file, BUCKET_NAME, f"{user.id}/{filename}/preview")
    await upload_video_db(filename, user.id)
    url = await get_presigned_url(filename)
    return {"url": url}


@router.get("/get_my_videos")
async def get_my_videos(count: int = 5, user: User = Depends(current_user)):
    urls = []
    videos = await get_user_video_models(user.id, count)
    for video in videos:
        urls.append(await get_presigned_url(f"{user.id}/{video.name}/video"))
    return urls


@router.get("/get_videos")
async def get_videos(user_id: int, count: int = 5):
    urls = []
    videos = await get_user_video_models(user_id, count)
    for video in videos:
        urls.append(await get_presigned_url(f"{user_id}/{video.name}/video"))
    return urls


#TODO(coder): session: AsyncSession = Depends(get_async_session)
async def get_user_video_models(user_id: int, count: int = 5):
    async with engine.begin() as connection:
        async_session = AsyncSession(bind=connection)
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


async def upload_video_db(filename: str, user_id: int):
    async with engine.begin() as connection:
        async_session = AsyncSession(bind=connection)
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

