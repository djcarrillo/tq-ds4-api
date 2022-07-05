import os
import boto3
from config.settings import Setting

path_base = os.path.dirname(os.path.realpath(__file__))


def init_dynamo_db():
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id=Setting.ACCESS_KEY_ID_AWS,
        aws_secret_access_key=Setting.SECRET_ACCESS_KEY_AWS,
        region_name='us-east-1'
    )

    return dynamodb