from config import config
from tools import local, cloud

if __name__ == "__main__":

    path = f'{config.desktop}\{config.name_folder}'
    files_to_upload = local.check_file(path)
    files_to_upload, list_to_delete = local.compare_json_locals(path, files_to_upload)
    cloud.upload_list(files_to_upload)
    local.update_json(files_to_upload, path)
    cloud.delete_objects(config.storage_bucket_name, list_to_delete)


