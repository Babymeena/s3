import boto3

def upload_file_to_s3(bucket_name, file_name, object_name=None):
    s3 = boto3.client('s3')

    if object_name is None:
        object_name = file_name

    s3.upload_file(file_name, bucket_name, object_name)
    print(f"File {file_name} uploaded to {bucket_name}/{object_name}")


upload_file_to_s3('example-bucket-0987651234', 'files.py')


