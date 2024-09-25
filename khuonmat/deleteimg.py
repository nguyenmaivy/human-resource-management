import os
import shutil
def delete():
    folder_path = 'khuonmat/data'

    shutil.rmtree(folder_path)

    os.makedirs(folder_path)