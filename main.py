from distutils import extension
import os
from file_extensions import folder_names
from pathlib import Path
import datetime as dt

download_path = 'c:/users/anujp/Downloads'
all_files = os.listdir(download_path)
# print(len(all_files))
files = [os.path.join(download_path,file) for file in all_files if os.path.isfile(os.path.join(download_path,file))]
folders = [os.path.join(download_path, file) for file in all_files if not os.path.isfile(os.path.join(download_path, file))]

# print(len(files),len(folders))

filetype_map={extension: filetype for filetype,extensions in folder_names.items() for extension in extensions}

def create_folder():
    folder_paths=[os.path.join(download_path,name,) for name in folder_names.keys()]
    [os.mkdir(folderPath) for folderPath in folder_paths if not os.path.exists(folderPath)]

def new_path(old_path):
    extension = str(old_path).split('.')[-1]
    folder = filetype_map[extension] if extension in filetype_map.keys() else 'Others'
    final_path = os.path.join(download_path, folder,str(old_path).split('\\')[-1])
    return final_path


create_folder()
[Path(file).rename(new_path(file)) for file in files]
[Path(folder).rename(os.path.join(download_path, 'Others', str(folder).split('\\')[-1])) for folder in folders if str(folder).split('\\')[-1] not in folder_names.keys() and str(folder).split('\\')[-1].split('_')[0] not in folder_names.keys()]
