import os
import shutil

def delete():
    folder_path = 'pydoan/khuonmat/saveid'

    # Kiểm tra danh sách tệp tin trong thư mục
    file_list = os.listdir(folder_path)
    
    if len(file_list) == 0:
        print("Không có tệp tin trong thư mục. Dừng chương trình.")
        return
    
    # Xóa toàn bộ nội dung trong thư mục
    shutil.rmtree(folder_path)

    # Tạo lại thư mục trống
    os.makedirs(folder_path)