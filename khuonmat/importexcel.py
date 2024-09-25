import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import DalStaff
def excel():
    def open_file_dialog():
        file_path = filedialog.askopenfilename()
        if file_path:
            # Đọc dữ liệu từ file Excel
            df = pd.read_excel(file_path)

            # Hiển thị thông báo cho người dùng
            print('Dữ liệu từ file Excel đã được đọc!')

            # Lưu trữ dữ liệu từ file Excel trong biến toàn cục
            global employee_data
            employee_data = df

            # Hiển thị dữ liệu lên bảng
            display_data(df)

    def addexcel(data):
        for row in treeview.get_children():
            treeview.delete(row)

        # Hiển thị dữ liệu từ DataFrame lên bảng
        for index, row in data.iterrows():
            HoTen = row['A']  # Update the column name
            NgaySinh = row['B']  # Update the column name
            GioiTinh = row['C']  # Update the column name
            Cmnd = row['D']  # Update the column name
            DiaChi = row['E']  # Update the column name
            ViTriCongViec = row['F']  # Update the column name
            PhongBan = row['G']  # Update the column name
            DalStaff.create_connection()
            DalStaff.insert_employee(HoTen, NgaySinh, GioiTinh, Cmnd, DiaChi, ViTriCongViec, PhongBan)

    def display_data(data):
        # Xóa dữ liệu cũ trong bảng
        for row in treeview.get_children():
            treeview.delete(row)

        # Hiển thị dữ liệu từ DataFrame lên bảng
        for index, row in data.iterrows():
            HoTen = row['A']  # Update the column name
            NgaySinh = row['B']  # Update the column name
            GioiTinh = row['C']  # Update the column name
            Cmnd = row['D']  # Update the column name
            DiaChi = row['E']  # Update the column name
            ViTriCongViec = row['F']  # Update the column name
            PhongBan = row['G']  # Update the column name

            treeview.insert('', 'end', values=(HoTen, NgaySinh, GioiTinh, Cmnd, DiaChi, ViTriCongViec, PhongBan))

    # Tạo cửa sổ giao diện
    window = tk.Tk()

    # Tạo nút "Open File"
    open_file_button = tk.Button(window, text="Open File", command=open_file_dialog)
    open_file_button.pack()

    # Tạo nút "Add to Database"
    add_to_db_button = tk.Button(window, text="Add to Database", command=lambda: addexcel(employee_data))
    add_to_db_button.pack()

    # Tạo Treeview để hiển thị dữ liệu
    treeview = ttk.Treeview(window, columns=('HoTen', 'NgaySinh', 'GioiTinh', 'Cmnd', 'DiaChi', 'ViTriCongViec', 'PhongBan'))
    treeview.pack()

    # Thiết lập header cho các cột
    treeview.heading('HoTen', text='Họ Tên')
    treeview.heading('NgaySinh', text='Ngày Sinh')
    treeview.heading('GioiTinh', text='Giới Tính')
    treeview.heading('Cmnd', text='CMND')
    treeview.heading('DiaChi', text='Địa Chỉ')
    treeview.heading('ViTriCongViec', text='Vị Trí Công Việc')
    treeview.heading('PhongBan', text='Phòng Ban')

    # Thiết lập độ rộng cột
    treeview.column('HoTen', width=100)
    treeview.column('NgaySinh', width=80)
    treeview.column('GioiTinh', width=80)
    treeview.column('Cmnd', width=100)
    treeview.column('DiaChi', width=150)
    treeview.column('ViTriCongViec', width=120)
    treeview.column('PhongBan', width=120)

    # Chạy vòng lặp chính của giao diện
    window.mainloop()