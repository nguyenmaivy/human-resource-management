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

# def insert_department(ma,ten):
#     """Thêm nhân viên vào cơ sở dữ liệu"""
#     global connection
#     insert_query = "INSERT INTO phongban(MaPhongBan,TenPhongBan) VALUES (%s, %s)"
#     data = (ma,ten)

#     try:
#         cursor = connection.cursor()
#         cursor.execute(insert_query, data)
#         connection.commit()
#         print('Thêm nhân vtcvtc!')
#     except Error as e:
#         print('Lỗi :', e)
# def get_mapb():
#     """Lấy danh sách tài khoản từ SQL"""
#     global connection
#     select_query = "SELECT MaPhongBan FROM phongban"
#     try:
#         cursor = connection.cursor()
#         cursor.execute(select_query)
#         vtri = cursor.fetchall()
#         return vtri
#     except Error as e:
#         print('Lỗi:', e)
# def get_all():
#     """Lấy danh sách tài khoản từ SQL"""
#     global connection
#     select_query = "SELECT * FROM phongban"
#     try:
#         cursor = connection.cursor()
#         cursor.execute(select_query)
#         vtri = cursor.fetchall()
#         return vtri
#     except Error as e:
#         print('Lỗi:', e)
# def get_tenpb(mapb):
#     """Lấy danh sách tài khoản từ SQL"""
#     global connection
#     select_query = "SELECT TenPhongBan FROM phongban where MaPhongBan= %s"
#     try:
#         cursor = connection.cursor()
#         cursor.execute(select_query,(mapb,))
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

def insert_department(ten):
    """Thêm nhân viên vào cơ sở dữ liệu"""
    global connection
    select_query = "SELECT COUNT(*) FROM phongban WHERE TenPhongBan = %s"
    insert_query = "INSERT INTO phongban(TenPhongBan) VALUES (%s)"
    data = (ten, )

    try:
        cursor = connection.cursor()
        cursor.execute(select_query, data)
        count = cursor.fetchone()[0]
        
        if count == 0:
            cursor.execute(insert_query, data)
            connection.commit()
            print('Thêm nhân viên thành công!')
        else:
            print('Phòng ban đã tồn tại!')
    except Error as e:
        print('Lỗi:', e)
def get_mapb():
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT MaPhongBan FROM phongban"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)
def get_tenpb(mapb):
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT TenPhongBan FROM phongban where MaPhongBan= %s"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query,(mapb,))
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)

def delete_department(ma):
    global connection
    query = 'Delete from phongban where MaPhongBan = %s'
    data = (ma, )

    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Xóa phòng ban thành công")
        return 0
    except Error as e:
        print("lỗi: ", e)
        return -1

def get_all_department():
    global connection
    query = 'Select  * From phongban'

    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("Lỗi: ", e)

def update_department(ma, ten):
    global connection
    query = 'update phongban set TenPhongBan = %s where MaPhongBan = %s'
    data = (ten, ma)

    try:
        cursor = connection.cursor()
        cursor.execute(query, data)
        connection.commit()
        print("Cập nhật thông tin phòng ban thành công!")
    except Error as e:
        print("Lỗi: ", e)