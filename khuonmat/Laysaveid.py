import os


def layid():
        folder_path = 'pydoan/khuonmat/saveid'
        file_list = os.listdir(folder_path)
        for file_name in file_list:
            name_without_extension = os.path.splitext(file_name)[0]
            return name_without_extension