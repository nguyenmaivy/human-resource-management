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


def insert_chamcong1(manv, ngay):
    """Thêm face_id vào cơ sở dữ liệu"""
    global connection
    insert_query = "INSERT INTO chamcong (MaNhanVien, NgayChamCong) SELECT %s, %s FROM dual WHERE NOT EXISTS (SELECT * FROM chamcong WHERE MaNhanVien = %s AND NgayChamCong = %s)"
    data = (manv, ngay, manv, ngay)

    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, data)
        connection.commit()
        if cursor.rowcount > 0:
            print('Chấm công thành công')
        else:
            print('Dữ liệu đã tồn tại')
    except Error as e:
        print('Lỗi khi chấm công:', e)
def get_chamcong(ma_nhan_vien, thang):
    """Lấy dữ liệu chấm công từ SQL cho một mã nhân viên và tháng cụ thể"""
    global connection
    select_query = "SELECT MaNhanVien, NgayChamCong FROM chamcong WHERE MaNhanVien = %s AND MONTH(NgayChamCong) = %s"

    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (ma_nhan_vien, thang))
        chamcong_data = cursor.fetchall()
        return chamcong_data
    except Error as e:
        print('Lỗi:', e)
def get_thangchamcong(ma_nhan_vien):
    """Lấy dữ liệu chấm công từ SQL cho một mã nhân viên cụ thể"""
    global connection
    select_query = "SELECT DISTINCT MONTH(NgayChamCong) AS ThangChamCong FROM chamcong WHERE MaNhanVien = %s"

    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (ma_nhan_vien,))
        thangchamcong_data = cursor.fetchall()
        return thangchamcong_data
    except Error as e:
        print('Lỗi:', e)

def get_thangchamcongkdk():
    """Lấy dữ liệu chấm công từ SQL cho một mã nhân viên cụ thể"""
    global connection
    select_query = "SELECT DISTINCT MONTH(NgayChamCong) AS ThangChamCong FROM chamcong"

    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        thangchamcong_data = cursor.fetchall()
        return thangchamcong_data
    except Error as e:
        print('Lỗi:', e)


def get_sochamcongtrongthang(thang):
    """Lấy dữ liệu chấm công từ SQL cho một mã nhân viên cụ thể"""
    global connection
    select_query = "SELECT chamcong.MaNhanVien, nhanvien.HoTen, vitricongviec.TenViTriCongViec, chamcong.SoNgayChamCong, vitricongviec.HeSoLuong FROM ( SELECT MaNhanVien, COUNT(NgayChamCong) AS SoNgayChamCong FROM chamcong WHERE MONTH(NgayChamCong) = %s GROUP BY MaNhanVien ) AS chamcong JOIN nhanvien ON chamcong.MaNhanVien = nhanvien.MaNhanVien JOIN vitricongviec ON nhanvien.ViTriCongViec = vitricongviec.MaViTriCongViec"
    
    try:
        cursor = connection.cursor()
        cursor.execute(select_query, (thang,))  # Chuyển tham số tháng thành tuple
        sochamcong = cursor.fetchall()
        return sochamcong
    except Error as e:
        print('Lỗi:', e)
def get_nhanvientaithang(manv,thang):
    """Lấy dữ liệu chấm công từ SQL cho một mã nhân viên cụ thể"""
    global connection
    select_query = "SELECT chamcong.MaNhanVien, nhanvien.HoTen, chamcong.NgayChamCong FROM chamcong JOIN nhanvien ON chamcong.MaNhanVien = nhanvien.MaNhanVien WHERE MONTH(chamcong.NgayChamCong) = %s AND chamcong.MaNhanVien = %s"
    data=(thang,manv)
    try:
        cursor = connection.cursor()
        cursor.execute(select_query,data)  # Chuyển tham số tháng thành tuple
        sochamcong = cursor.fetchall()
        return sochamcong
    except Error as e:
        print('Lỗi:', e)


