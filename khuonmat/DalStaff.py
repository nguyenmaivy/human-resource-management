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

def insert_employee(HoTen, NgaySinh, GioiTinh, Cmnd, DiaChi, ViTriCongViec, PhongBan):
    """Thêm nhân viên vào cơ sở dữ liệu"""
    global connection
    select_query = "SELECT COUNT(*) FROM nhanvien WHERE Cmnd = %s"
    insert_query = "INSERT INTO nhanvien(HoTen, NgaySinh, GioiTinh, Cmnd, DiaChi, ViTriCongViec, PhongBan) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (HoTen, NgaySinh, GioiTinh, Cmnd, DiaChi, ViTriCongViec, PhongBan)

    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (Cmnd,))
        count = cursor.fetchone()[0]

        if count == 0:
            cursor.execute(insert_query, data)
            connection.commit()
            print('Thêm nhân viên thành công!')
        else:
            print('Nhân viên đã tồn tại!')
            return 0
    except Error as e:
        print('Lỗi thêm nhân viên:', e)
def update_employee(manv, HoTen, NgaySinh, GioiTinh, Cmnd, DiaChi, ViTriCongViec, PhongBan):
    """Cập nhật thông tin nhân viên trong cơ sở dữ liệu"""
    print(manv, HoTen, NgaySinh, GioiTinh, Cmnd, DiaChi, ViTriCongViec, PhongBan)
    global connection
    update_query = "UPDATE nhanvien SET HoTen = %s, NgaySinh = %s, GioiTinh = %s, Cmnd = %s, DiaChi = %s, ViTriCongViec = %s, PhongBan = %s WHERE MaNhanVien = %s"
    data = (HoTen, NgaySinh, GioiTinh, Cmnd, DiaChi, ViTriCongViec, PhongBan, manv)

    try:
        cursor = connection.cursor()
        cursor.execute(update_query, data)
        connection.commit()
        print('Cập nhật nhân viên thành công!')
    except Error as e:
        print('Lỗi cập nhật nhân viên:', e)

def get_idnv(ten,ma):
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT `MaNhanVien`FROM `nhanvien` WHERE HoTen =%s and Cmnd =%s"
    data=(ten,(ma))
    try:
        cursor = connection.cursor()
        cursor.execute(select_query,data)
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)
def get_allnv():
    global connection
    select_query = "SELECT * FROM `nhanvien`"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)
def get_ablefaceid():
    global connection
    select_query = "SELECT n.MaNhanVien, n.HoTen, CASE WHEN f.MaNhanVien IS NOT NULL THEN 1 ELSE 0 END AS TonTai FROM nhanvien n LEFT JOIN facaid f ON n.MaNhanVien = f.MaNhanVien"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)

def get_idkdk():
    """Lấy danh sách tài khoản từ SQL"""
    global connection
    select_query = "SELECT `MaNhanVien`FROM `nhanvien`"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)
def getten(manv):
    """Lấy tên nhân viên từ SQL"""
    select_query = "SELECT HoTen FROM nhanvien WHERE MaNhanVien = %s"
    global connection
    try:
        cursor = connection.cursor()
        cursor.execute(select_query,(manv,))
        vtri = cursor.fetchall()
        return vtri
    except Error as e:
        print('Lỗi:', e)

def delete_employee(manv):
    """Xóa nhân viên từ cơ sở dữ liệu"""
    global connection
    delete_query = "DELETE FROM `nhanvien` WHERE MaNhanVien=%s"
    data = (manv,)

    try:
        cursor = connection.cursor()
        cursor.execute(delete_query, data)
        connection.commit()
        print('Xóa nhân viên thành công!')
        return 0  # Trả về 0 để chỉ ra xóa thành công
    except Error as e:
        print('Lỗi xóa nhân viên:', e)
        return -1  # Trả về -1 để chỉ ra lỗi xóa nhân viên
    
def getname(manv):
    """Lấy tên nhân viên từ SQL"""
    select_query = "SELECT HoTen FROM nhanvien WHERE MaNhanVien = %s"
    global connection
    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (manv,))
        vtri = cursor.fetchall()
        if vtri:
            ten = vtri[0][0]
            return ten
        else:
            return None
    except Error as e:
        print('Lỗi:', e)
def close_connection():
    """Đóng kết nối đến cơ sở dữ liệu MySQL"""
    global connection
    if connection.is_connected():
        connection.close()
        print('Kết nối đã được đóng!')
