import boto3
import uuid
from core.config import settings

_s3 = None

def _get_client():
    global _s3
    if _s3 is None:
        _s3 = boto3.client(
            "s3",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
    return _s3

def upload_bytes(data: bytes, s3_key: str, content_type: str = "image/png") -> str:
    s3 = _get_client()
    s3.put_object(
        Bucket=settings.S3_BUCKET,
        Key=s3_key,
        Body=data,
        ContentType=content_type,
    )
    return s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': settings.S3_BUCKET, 'Key': s3_key},
        ExpiresIn=3600
    )

def upload_file(local_path: str, s3_key: str) -> str:
    s3 = _get_client()
    s3.upload_file(local_path, settings.S3_BUCKET, s3_key)
    return s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': settings.S3_BUCKET, 'Key': s3_key},
        ExpiresIn=3600
    )

def generate_key(prefix: str, ext: str = "png") -> str:
    return f"{prefix}/{uuid.uuid4().hex}.{ext}"