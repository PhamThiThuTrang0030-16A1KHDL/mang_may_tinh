import boto3 
from botocore.client import Config 
 
s3 = boto3.client('s3', 
    endpoint_url='http://127.0.0.1:9000', 
    aws_access_key_id='Hoàng_sy_viet_22174600094', 
    aws_secret_access_key='12345678', 
    config=Config(signature_version='s3v4'), 
    region_name='us-east-1') 
 
s3.download_file('iot-lab-demo', 'sensor_data.csv', 'temp.csv') 
print("Download thành công!") 