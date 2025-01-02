import json
import boto3

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    for record in event['Records']:
        # Kinesis 데이터 디코딩
        payload = json.loads(record['kinesis']['data'])
        
        # 민감한 데이터 제거
        payload.pop('sensitive_field', None)
        
        # DynamoDB에 저장
        dynamodb.put_item(
            TableName='Transactions',
            Item={
                'TransactionID': {'S': payload['transaction_id']},
                'Details': {'S': json.dumps(payload)}
            }
        )
    return {'status': 'success'}
