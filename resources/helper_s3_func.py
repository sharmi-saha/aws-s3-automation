import time

import pytest
from matplotlib import pyplot as plt
import logging as logger


def create_new_bucket(s3, name):
    if name not in list_available_buckets(s3):
        logger.info(f"'{name}' bucket does not exist, creating now")
        try:
            s3.create_bucket(Bucket=name)
        except Exception as e:
            logger.error(e)
            pytest.fail()
        logger.info(f"'{name}' bucket has been created")
    else:
        delete_bucket(s3, name)
        create_new_bucket(s3, name)


def list_available_buckets(s3):
    try:
        all_buckets = [bucket.name for bucket in s3.buckets.all()]
    except Exception as e:
        logger.error(e)
        pytest.fail()
    return all_buckets


def delete_bucket(s3, name: str):
    if name in list_available_buckets(s3):
        logger.info(f"'{name}' bucket does exist, deleting now")
        delete_all_files_from_s3_bucket(s3, name)
        try:
            bucket = s3.Bucket(name)
            bucket.delete()
        except Exception as e:
            logger.error(e)
            pytest.fail()
        logger.info(f"'{name}' bucket has been deleted")
    else:
        logger.info(f"'{name}' bucket does not exist")


def delete_all_files_from_s3_bucket(s3, bucket_name):
    for f in s3.Bucket(bucket_name).objects.all():
        logger.info(f"deleting the file")
        try:
            s3.Object(bucket_name, f.key).delete()
        except Exception as e:
            logger.error(e)
            pytest.fail()


def upload_file_in_s3_bucket(s3, bucket_name, file_name):
    logger.info("started uploading file")
    try:
        s3.Bucket(bucket_name).upload_file(Filename=file_name, Key=file_name)
    except Exception as e:
        logger.error(e)
        pytest.fail()


def download_file_from_s3_bucket(s3, bucket_name, file_name, download_file_name):
    logger.info(f"downloading the file")
    try:
        s3.Bucket(bucket_name).download_file(file_name, download_file_name)
    except Exception as e:
        logger.error(e)
        pytest.fail()


def delete_file_from_s3_bucket(s3, bucket_name, file_name):
    logger.info(f"deleting the file {file_name}")
    s3.Object(bucket_name, file_name).delete()


def show_aws_s3_file_upload_performance(s3, files, bucket, save_file):
    upload_times = []
    logger.info("uploading the files")
    for f in files:
        past = int(time.time_ns())
        upload_file_in_s3_bucket(s3, bucket, f)
        now = int(time.time_ns())
        time_taken = (now-past)/1000000
        upload_times.append(time_taken)
    logger.info(files)
    logger.info(upload_times)
    plt.bar(files, upload_times)
    plt.title("Bar Chart Plot")
    plt.xlabel('file_name')
    plt.ylabel('upload_time(ms)')
    plt.savefig(save_file)
