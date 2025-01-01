import boto3

client = boto3.client('rds')
token = client.generate_db_auth_token(
    DBHostname='db-endpoint',
    Port=3306,
    DBUsername='iam_user'
)
print(f"Generated Token: {token}")
