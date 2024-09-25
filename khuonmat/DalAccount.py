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
def insert_account(manv, mk, pq):
    """Thêm tài khoản vào bảng taikhoan mà không cho phép trùng lặp"""
    global connection
    insert_query = "INSERT INTO taikhoan(MaNhanVien, MatKhau, phanquyen) SELECT %s, %s, %s FROM DUAL WHERE NOT EXISTS (SELECT * FROM taikhoan WHERE MaNhanVien = %s)"
    data = (manv, mk, pq, manv)

    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, data)
        connection.commit()
        if cursor.rowcount > 0:
            print('Thêm thành công!')
        else:
            print('Tài khoản đã tồn tại và không được thêm vào.')
    except Error as e:
        print('Lỗi:', e)

def update_account(manv, mk, pq):
    """Cập nhật thông tin tài khoản trong SQL"""
    global connection
    update_query = "UPDATE taikhoan SET MatKhau = %s, phanquyen = %s WHERE MaNhanVien = %s"
    data = (mk, pq, manv)

    try:
        cursor = connection.cursor()
        cursor.execute(update_query, data)
        connection.commit()
        print('Cập nhật thành công!')
    except Error as e:
        print('Lỗi:', e)

def delete_account(manv):
    """Xóa tài khoản khỏi SQL"""
    global connection
    delete_query = "DELETE FROM taikhoan WHERE MaNhanVien = %s"
    data = (manv,)

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, data)
        connection.commit()
        print('Xóa thành công!')
    except Error as e:
        print('Lỗi:', e)

def get_accounts():
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT * FROM taikhoan"

    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        accounts = cursor.fetchall()
        return accounts
    except Error as e:
        print('Lỗi:', e)

def get_accountmanager():
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT taikhoan.MaNhanVien,nhanvien.HoTen,taikhoan.MatKhau,taikhoan.phanquyen FROM taikhoan,nhanvien WHERE taikhoan.MaNhanVien=nhanvien.MaNhanVien"

    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        accounts = cursor.fetchall()
        return accounts
    except Error as e:
        print('Lỗi:', e)
def laymanhanvien():
    global connection
    select_query = "SELECT MaNhanVien FROM nhanvien"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        accounts = cursor.fetchall()
        return accounts
    except Error as e:
        print('Lỗi:', e)