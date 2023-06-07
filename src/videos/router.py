import logging
from botocore.exceptions import ClientError
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from config import BUCKET_NAME, ALLOWED_FILE_EXTENSIONS
from database import get_async_session
import boto3

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

router = APIRouter(
    prefix="/videos",
    tags=["Video"]
)


async def create_presigned_url(video_name: str):
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

    return {"url": response}


@router.post("/post_video")
async def post_video(file: UploadFile = File()):
    file_name = file.filename
    if not any(file_name.endswith(ext) for ext in ALLOWED_FILE_EXTENSIONS):
        raise HTTPException(status_code=400, detail="Invalid file type")
    s3.upload_fileobj(file.file, BUCKET_NAME, file_name)
    url = await create_presigned_url(file_name)
    return url


async def upload_video_db(file: UploadFile = File()):
    pass

