import os
from pathlib import Path
import datetime as dt
from typing import final
download_path = 'c:/users/anujp/Downloads'
from file_extensions import folder_names
# all_files = os.listdir(download_path)
# Path('c:/users/anujp/Downloads/Code/app.js').stat().st_ctime
currenttime= dt.datetime.timestamp(dt.datetime.now())

def get_month(timestamp):
    dt_object = dt.datetime.fromtimestamp(timestamp)
    month=dt_object.month
    year=dt_object.year
    return f'{month}-{year}'

def new_path(old_path):
    mmyy=get_month(Path(old_path).stat().st_ctime)
    folder = mmyy+'_'+old_path.split('\\')[-2]
    if not os.path.exists(os.path.join(download_path, folder)):
        os.mkdir(os.path.join(download_path, folder))
    final_path = os.path.join(download_path, folder, old_path.split('\\')[-1])
    return final_path



folder_path = [os.path.join(download_path, folder) for folder in folder_names.keys()]
old_files=[]
for folder in folder_path:
    old_files.append([os.path.join(folder, file) for file in os.listdir(folder) if currenttime-Path(os.path.join(folder, file)).stat().st_ctime >= 15778458])

for file in old_files:
    [Path(file_type).rename(new_path(file_type)) for file_type in file]
# print(len(old_files))
