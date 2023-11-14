import os

# local
name_folder = 'cloud'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
appdata = os.path.join(os.path.join(os.environ['USERPROFILE']), 'AppData')
main_file_name = 'main.py'
path_to_object = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]+'/objects/files_in_cloud.json'
script_name = "cloud_script.bat"
#cloud 
path_to_json = "LOCATION_OF_YOUR_KEY"
storage_bucket_name = "Your_bucket_name"
bucket_location = "EUROPE-WEST1"
type_bucket = "COLDLINE"
project_name = "YOUR_PROJECT_NAME"
