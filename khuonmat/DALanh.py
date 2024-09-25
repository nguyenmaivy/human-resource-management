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

def insert_face_id(mafaceid, manv, tenanh):
    """Thêm face_id vào cơ sở dữ liệu"""
    global connection
    insert_query = "INSERT INTO facaid(Maface, MaNhanVien, Tenanh) VALUES (%s, %s, %s)"
    data = (mafaceid, manv, tenanh)

    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, data)
        connection.commit()
        print('Thêm face_id thành công!')
    except Error as e:
        print('Lỗi thêm face_id:', e)
def get_all_records():
    """Lấy tất cả các bản ghi từ bảng facaid"""
    global connection
    select_query = "SELECT MaNhanVien, ten FROM facaid"

    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        records = cursor.fetchall()
        transformed_records = [f"{record[1]}-{record[0]}" for record in records]
        return transformed_records
    except Error as e:
        print('Lỗi truy vấn:', e)
        return []
def get_all_names():
    """Lấy tất cả các tên từ bảng facaid"""
    global connection
    select_query = "SELECT ten FROM facaid"

    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        records = cursor.fetchall()
        transformed_records = [record[0] for record in records]
        return transformed_records
    except Error as e:
        print('Lỗi truy vấn:', e)
        return []
