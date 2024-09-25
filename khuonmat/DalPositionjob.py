# import mysql.connector
# from mysql.connector import Error

# connection = None

# def create_connection():
#     """Tạo kết nối đến cơ sở dữ liệu MySQL"""
#     global connection
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             database='staffmanager',
#             user='root',
#             password=''
#         )
#         if connection.is_connected():
#             print('Kết nối thành công!')
#     except Error as e:
#         print('Lỗi kết nối:', e)

# def insert_positionjob(maViTriCongViec,viTriCongViec):
#     """Thêm nhân viên vào cơ sở dữ liệu"""
#     global connection
#     insert_query = "INSERT INTO vitricongviec(MaViTriCongViec,TenViTriCongViec) VALUES (%s, %s)"
#     data = (maViTriCongViec,viTriCongViec)

#     try:
#         cursor = connection.cursor()
#         cursor.execute(insert_query, data)
#         connection.commit()
#         print('Thêm nhân vtcvtc!')
#     except Error as e:
#         print('Lỗi :', e)
# def get_macv():
#     """Lấy danh sách tài khoản từ SQL"""
#     global connection
#     select_query = "SELECT `MaViTriCongViec` FROM `vitricongviec`"
#     try:
#         cursor = connection.cursor()
#         cursor.execute(select_query)
#         vtri = cursor.fetchall()
#         return vtri
#     except Error as e:
#         print('Lỗi:', e)
# def get_tencv(macv):
#     """Lấy danh sách tài khoản từ SQL"""
#     global connection
#     select_query = "SELECT `TenViTriCongViec` FROM `vitricongviec` WHERE MaViTriCongViec =%s"
#     try:
#         cursor = connection.cursor()
#         cursor.execute(select_query,(macv,))
#         vtri = cursor.fetchall()
#         return vtri
#     except Error as e:
#         print('Lỗi:', e)

import mysql.connector
from mysql.connector import Error

connection = None

def create_connection():
    """Tạo kết nối đến cơ sở dữ liệu MySQL"""
    global connection
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='staffmanager',
            user='root',
            password=''
        )
        if connection.is_connected():
            print('Kết nối thành công!')
    except Error as e:
        print('Lỗi kết nối:', e)

def insert_positionjob(macv,tencv, hesoluong):
    """Thêm nhân viên vào cơ sở dữ liệu"""
    global connection
    select_query = "SELECT COUNT(*) FROM vitricongviec WHERE TenViTriCongViec = %s"
    insert_query = "INSERT INTO vitricongviec(MaViTriCongViec,TenViTriCongViec, HeSoLuong) VALUES (%s,%s, %s)"
    data = (macv,tencv, hesoluong)

    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (tencv,))
        count = cursor.fetchone()[0]
        
        if count == 0:
            cursor.execute(insert_query, data)
            connection.commit()
            print('Thêm nhân viên thành công!')
        else:
            print('Vị trí công việc đã tồn tại!')
    except Error as e:
        print('Lỗi:', e)
def get_macv1():
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT MaViTriCongViec FROM vitricongviec"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)
def get_macv():
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT MaViTriCongViec FROM vitricongviec"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)
def get_tencv(macv):
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT TenViTriCongViec, HeSoLuong FROM vitricongviec WHERE MaViTriCongViec =%s"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query,(macv,))
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)

def update_positionjob(macv, tencv, heSoLuong):
    """Cập nhật thông tin vị trí công việc trong SQL"""
    global connection
    update_query = "UPDATE vitricongviec SET TenViTriCongViec = %s, HeSoLuong = %s WHERE MaViTriCongViec = %s"
    data = (tencv, heSoLuong, macv)

    try:
        cursor = connection.cursor()
        cursor.execute(update_query, data)
        connection.commit()
        print('Cập nhật thành công!')
    except Error as e:
        print('Lỗi:', e)

def delete_positionjob(macv):
    """Xóa mã vị trí công việc khỏi SQL"""
    global connection
    delete_query = "DELETE FROM vitricongviec WHERE MaViTriCongViec = %s"
    data = (macv,)

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, data)
        connection.commit()
        print('Xóa thành công!')
    except Error as e:
        print('Lỗi:', e)

def update_positionjob(macv, tencv, heSoLuong):
    """Cập nhật thông tin vị trí công việc trong SQL"""
    global connection
    update_query = "UPDATE vitricongviec SET TenViTriCongViec = %s, HeSoLuong = %s WHERE MaViTriCongViec = %s"
    data = (tencv, heSoLuong, macv)

    try:
        cursor = connection.cursor()
        cursor.execute(update_query, data)
        connection.commit()
        print('Cập nhật thành công!')
    except Error as e:
        print('Lỗi:', e)

def delete_positionjob(macv):
    """Xóa mã vị trí công việc khỏi SQL"""
    global connection
    delete_query = "DELETE FROM vitricongviec WHERE MaViTriCongViec = %s"
    data = (macv,)

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, data)
        connection.commit()
        print('Xóa thành công!')
    except Error as e:
        print('Lỗi:', e)
def get_all_positionjob():
    global connection
    query = 'Select  * From vitricongviec'

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("Lỗi: ", e)
