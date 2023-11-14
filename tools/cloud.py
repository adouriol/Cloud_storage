from google.cloud import storage
from google.cloud.storage import transfer_manager
import os 
from config import config

def create_storage():
    #Creates a bucket depending on the config files variables
    os.environ["google_credentials"] = config.path_to_json
    project_id, bucket_name = config.project_name, config.storage_bucket_name
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = config.type_bucket
    bucket.create(project = project_id, location = config.bucket_location )

def upload_list(list_to_upload):

    def upload_many_blobs_with_transfer_manager(bucket_name, filenames, source_directory=f'{config.desktop}\{config.name_folder}', workers=8):
        #Upload blobs
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        results = transfer_manager.upload_many_from_filenames(bucket, filenames, source_directory = source_directory, max_workers = workers)

        for name, result in zip(filenames, results):
            if isinstance(result, Exception):
                print("Failed to upload {} due to exception: {}".format(name, result))
            else:
                print("Uploaded {} to {}.".format(name, bucket.name))

    def upload_blob(bucket_name, list_to_upload):
        #Upload blobs
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        for i in list_to_upload:
            destination_blob_name = i.split('/')[-1]
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(f'{config.desktop}\{config.name_folder}/{i}')
            print( f"File {i} uploaded to {destination_blob_name}.")
 
    if len(list_to_upload) >10 : return upload_many_blobs_with_transfer_manager(config.storage_bucket_name,list_to_upload)
    else: return upload_blob(config.storage_bucket_name,list_to_upload) 

def delete_objects(bucket_name, list_of_blobs):
    #Deletes a blob from the bucket
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    for i in list_of_blobs:
        blob = bucket.blob(i)
        blob.delete()
        print(f"Blob {i} deleted.")