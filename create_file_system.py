from tools import local, cloud

def create_file_system():
    local.create_repository()
    cloud.create_storage()
    local.add_to_startup(file_path= __file__)
    print("Just created your cloud storage and your cloud file")
    
create_file_system()