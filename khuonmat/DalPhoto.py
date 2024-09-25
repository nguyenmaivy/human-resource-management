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

def insert_face_id(mafaceid, manv,  ten):
    """Thêm face_id vào cơ sở dữ liệu"""
    global connection
    insert_query = "INSERT INTO facaid(Maface, MaNhanVien,  ten) VALUES (%s, %s, %s)"
    data = (mafaceid, manv,  ten)

    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, data)
        connection.commit()
        print('Thêm face_id thành công!')
    except Error as e:
        print('Lỗi thêm face_id:', e)
def get_all_names():
    """Lấy tất cả các tên từ cơ sở dữ liệu và trả về một danh sách"""
    global connection
    select_query = "SELECT ten FROM facaid"

    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        records = cursor.fetchall()
        names = [record[0] for record in records]
        return names
    except Error as e:
        print('Lỗi lấy dữ liệu:', e)
        return []
def get_ten(manv):
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT ten FROM facaid WHERE MaNhanVien= %s"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (manv,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except Error as e:
        print('Lỗi:', e)
def check_id_exists(manv):
    """Kiểm tra xem ID có tồn tại trong cơ sở dữ liệu hay không"""
    global connection
    select_query = "SELECT COUNT(*) FROM facaid WHERE MaNhanVien = %s"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (manv,))
        count = cursor.fetchone()[0]
        if count > 0:
            return 1
        else:
            return 0
    except Error as e:
        print('Lỗi:', e)