import os 
import subprocess
from config import config
import json 

def create_repository():
    # If the directory doesn't exist it will create it
    if os.path.isdir(f'{config.desktop}\{config.name_folder}') == False: subprocess.call(f'mkdir {config.desktop}\{config.name_folder}', shell=True)

def check_file(path):
    #Compare the files in a folder with a json
    directoriy_list = os.listdir(path)
    with open(config.path_to_object) as f:
        json_file = json.load(f)
    cloud_file = [i['Name'] for i in json_file['files']]
    set_differences = set(directoriy_list) - set(cloud_file)
    return  list(set_differences)

def compare_json_locals(path: str ,list_to_upload :list):

    list_to_delete = []
    with open(config.path_to_object) as f:
        json_file = json.load(f)
    if len(json_file['files'])>0:
        for i in range(len(json_file['files'])):
            try:
                if os.path.getmtime(path + '/' + json_file['files'][i]['Name']) != json_file['files'][i]['Modified time']: list_to_upload.append(json_file['files'][i]['Name'])
            except: list_to_delete.append(json_file['files'][i]['Name'])
            
    return list_to_upload, list_to_delete

def update_json(list_of_files, path:str ):

    if len(list_of_files) == 0:
        print('Nothing to update')
        pass
    to_insert = []
    for i in list_of_files:
        path_to_file = path +'/'+ i
        size = os.path.getsize(path_to_file)
        created = os.path.getctime(path_to_file)
        modified = os.path.getmtime(path_to_file)
        name = i
        to_insert.append({'Name': name, 'created_time': created, 'Modified time': modified, 'Size': size})
    
    with open(config.path_to_object) as data_file:
        json_file = json.load(data_file)
    [json_file['files'].append(j) for j in to_insert]
    with open(config.path_to_object, 'w') as outfile:
        json.dump(json_file, outfile)

def add_to_startup(file_path=""):

    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = f'{config.appdata}\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' 
    file_path  = os.path.split(file_path)[0]+'/' +config.main_file_name
    with open(bat_path + '\\' + config.script_name, "w+") as bat_file:
        bat_file.write(r'python "%s"' % file_path)