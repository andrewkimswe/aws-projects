import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # S3에서 이미지 다운로드
        response = s3.get_object(Bucket=bucket, Key=key)
        img = Image.open(io.BytesIO(response['Body'].read()))

        # 이미지 압축
        compressed_img = io.BytesIO()
        img.save(compressed_img, format='JPEG', quality=50)
        compressed_img.seek(0)

        # 압축된 이미지 저장
        compressed_bucket = 'compressed-images-bucket'
        s3.put_object(Bucket=compressed_bucket, Key=f'compressed/{key}', Body=compressed_img)
    
    return {'status': 'success'}
