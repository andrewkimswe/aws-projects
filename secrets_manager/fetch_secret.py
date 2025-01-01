import boto3

client = boto3.client('secretsmanager')
response = client.get_secret_value(SecretId='your-secret-id')
secret = response['SecretString']
print(f"Fetched Secret: {secret}")
