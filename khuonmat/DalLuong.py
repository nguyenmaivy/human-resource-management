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

def insert(manv, thang, tien):
    """Thêm tai khoan vao sql"""
    global connection
    insert_query = "INSERT INTO `luong` (MaNhanVien, Thang, tien) SELECT %s, %s, %s FROM `luong` WHERE NOT EXISTS (SELECT * FROM `luong` WHERE MaNhanVien = %s AND Thang = %s)"
    data = (manv, thang, tien, manv, thang)

    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, data)
        connection.commit()
        print('Thêm thành công!')
    except Error as e:
        print('Lỗi:', e)
def get_thang(manv):
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT Thang FROM `luong` WHERE MaNhanVien= %s"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (manv,))
        accounts = cursor.fetchall()
        return accounts
    except Error as e:
        print('Lỗi:', e)

def get_luong(manv,thang):
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT tien FROM `luong` WHERE MaNhanVien= %s and Thang=%s"
    data=(manv,thang)
    try:
        cursor = connection.cursor()
        cursor.execute(select_query,data)
        accounts = cursor.fetchall()
        return accounts
    except Error as e:
        print('Lỗi:', e)