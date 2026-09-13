# core/supabase_storage.py
"""
Uploads files to a Supabase Storage bucket using Supabase's S3-compatible
protocol (via boto3) — the same approach used on the Rina Tours project.

Settings required (see .env.example):
    SUPABASE_URL                    e.g. https://gkzotofslqdfoqagobkh.supabase.co
    SUPABASE_S3_ACCESS_KEY_ID       From Supabase dashboard -> Storage -> S3 Connection
    SUPABASE_S3_SECRET_ACCESS_KEY   Same place
    SUPABASE_S3_REGION              e.g. eu-central-1
    SUPABASE_STORAGE_BUCKET         Bucket name, e.g. "product-images"

The bucket must exist and be set to "Public" so the returned URLs work
directly in <img> tags.
"""
import mimetypes
import uuid

import boto3
import requests
from botocore.client import Config
from django.conf import settings


def _project_ref():
    # https://gkzotofslqdfoqagobkh.supabase.co -> gkzotofslqdfoqagobkh
    host = settings.SUPABASE_URL.rstrip('/').split('//')[-1]
    return host.split('.')[0]


def _s3_client():
    endpoint = f"https://{_project_ref()}.supabase.co/storage/v1/s3"
    return boto3.client(
        's3',
        endpoint_url=endpoint,
        aws_access_key_id=settings.SUPABASE_S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings.SUPABASE_S3_SECRET_ACCESS_KEY,
        region_name=settings.SUPABASE_S3_REGION,
        config=Config(s3={'addressing_style': 'path'}, signature_version='s3v4'),
    )


def upload_bytes(data, filename, content_type=None, bucket=None):
    """
    Uploads raw bytes to the Supabase Storage bucket and returns the
    public URL. A random name is generated so uploads never collide.
    """
    bucket = bucket or settings.SUPABASE_STORAGE_BUCKET
    content_type = content_type or mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    ext = filename.rsplit('.', 1)[-1].split('?')[0] if '.' in filename else 'jpg'
    path = f"{uuid.uuid4().hex}.{ext}"

    client = _s3_client()
    client.put_object(Bucket=bucket, Key=path, Body=data, ContentType=content_type)

    return f"{settings.SUPABASE_URL.rstrip('/')}/storage/v1/object/public/{bucket}/{path}"


def upload_django_file(django_file, bucket=None):
    """Uploads a Django UploadedFile (from an admin form) and returns the public URL."""
    data = django_file.read()
    content_type = getattr(django_file, 'content_type', None)
    return upload_bytes(data, django_file.name, content_type, bucket=bucket)


def is_supabase_url(value):
    """True if `value` already points at our Supabase Storage bucket."""
    return bool(value) and '/storage/v1/object/public/' in value


def download_uploadcare(value):
    """
    Downloads an image previously stored via Uploadcare. `value` may be a
    bare UUID or a full CDN URL (ucarecdn.com or a custom branded domain
    like xxxxx.ucarecd.net both work the same way).
    Returns (bytes, content_type, error). `error` is None on success, or
    the exception message on failure.
    """
    if not value:
        return None, None, "empty value"
    base = value.rstrip('/')
    if not base.startswith('http'):
        base = f"https://ucarecdn.com/{base}"
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/120.0 Safari/537.36'
        ),
        'Accept': 'image/*,*/*;q=0.8',
    }
    try:
        resp = requests.get(base, timeout=20, headers=headers, allow_redirects=True)
        resp.raise_for_status()
        return resp.content, resp.headers.get('Content-Type', 'image/jpeg'), None
    except requests.RequestException as e:
        return None, None, str(e)
