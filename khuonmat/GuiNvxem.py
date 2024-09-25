import tkinter as tk
from tkinter import ttk
import DalStaff

def create_table():
    """Tạo bảng nhân viên"""
    root = tk.Tk()
    root.title('Bảng nhân viên')
    root.geometry('700x400')
    table = ttk.Treeview(root, columns=('MaNhanVien', 'HoTen', 'NgaySinh', 'GioiTinh', 'Cmnd', 'DiaChi', 'ViTriCongViec', 'PhongBan'), show='headings')
    table.pack(fill='both', expand=True)
    table.heading('MaNhanVien', text='Mã NV')
    table.heading('HoTen', text='Họ tên')
    table.heading('NgaySinh', text='Ngày sinh')
    table.heading('GioiTinh', text='Giới tính')
    table.heading('Cmnd', text='CMND')
    table.heading('DiaChi', text='Địa chỉ')
    table.heading('ViTriCongViec', text='Vị trí công việc')
    table.heading('PhongBan', text='Phòng ban')
    table.column('MaNhanVien', width=80)
    table.column('HoTen', width=150)
    table.column('NgaySinh', width=80)
    table.column('GioiTinh', width=80)
    table.column('Cmnd', width=80)
    table.column('DiaChi', width=80)
    table.column('ViTriCongViec', width=80)
    table.column('PhongBan', width=80)
    DalStaff.create_connection()
    data = DalStaff.get_allnv()
    for row in data:
        table.insert('', 'end', values=row)

    root.mainloop()
