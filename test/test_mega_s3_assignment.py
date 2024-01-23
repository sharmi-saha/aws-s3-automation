from data import config
from resources import helper_s3_func as helper

# 1. Create a aws s3 bucket


def test_create_aws_s3_bucket(s3_resource, name=config.BUCKET_NAME):
    helper.create_new_bucket(s3_resource, name)


#   2. Upload a text file

def test_upload_txt_file_in_s3_bucket(s3_resource, bucket_name=config.BUCKET_NAME, file_name=config.FILE_NAME_1):
    helper.upload_file_in_s3_bucket(s3_resource, bucket_name, file_name)


#   3. Download the text file

def test_download_file_from_s3_bucket(s3_resource, bucket_name=config.BUCKET_NAME, file_name=config.FILE_NAME_1, download_file_name=config.DOWNLOAD_FILE):
    helper.download_file_from_s3_bucket(s3_resource, bucket_name, file_name, download_file_name)


#   4. Delete the text file

def test_delete_file_from_s3_bucket(s3_resource, bucket_name=config.BUCKET_NAME, file_name=config.FILE_NAME_1):
    helper.delete_file_from_s3_bucket(s3_resource, bucket_name, file_name)


#   5. Prepare a report for file upload performance, data visulization methods are preferred

def test_prepare_report_for_file_upload_performance(s3_resource, files=config.FILES, bucket=config.BUCKET_NAME, save_file=config.SAVE_IMAGE_FILE):
    helper.show_aws_s3_file_upload_performance(s3_resource, files, bucket, save_file)


