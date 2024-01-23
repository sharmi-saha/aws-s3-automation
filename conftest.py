import base64
from pytest import fixture
import boto3
from data import config
import logging


@fixture(scope='session')
def s3_resource():
    logging.info("creating s3 resource")
    DEC_ACCESS_KEY = base64_decode(config.ACCESS_KEY)
    DEC_SECRET_KEY = base64_decode(config.SECRET_KEY)
    s3 = boto3.resource('s3', aws_access_key_id=DEC_ACCESS_KEY, aws_secret_access_key=DEC_SECRET_KEY)
    return s3


def base64_decode(string_to_decode: str):
    decoded_string = base64.b64decode(string_to_decode).decode('utf-8')
    return decoded_string
