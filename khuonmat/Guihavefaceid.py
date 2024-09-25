import tkinter as tk
from tkinter import ttk
import mysql.connector
import DalStaff

# Kết nối đến cơ sở dữ liệu

# Tạo giao diện Tkinter
def tinhtrang():
    root = tk.Tk()

    root.title("Dữ liệu nhân viên")
    root.geometry("500x250")
    text = tk.Label(root, text="Tình trạng dữu liệu ",   font=("Arial", 20))
    text.pack()


    # Tạo bảng dữ liệu
    table = ttk.Treeview(root, columns=("Mã nhân viên", "Tên nhân viên", "Dữ liệu khuôn mặt"), show="headings")
    table.heading("Mã nhân viên", text="Mã nhân viên")
    table.heading("Tên nhân viên", text="Tên nhân viên")
    table.heading("Dữ liệu khuôn mặt", text="Dữ liệu khuôn mặt")

    # Lấy dữ liệu từ cơ sở dữ liệu
    DalStaff.create_connection()
    data = DalStaff.get_ablefaceid()

    # Đưa dữ liệu lên bảng
    for row in data:
        table.insert("", "end", values=row)

    # Định dạng cột
    table.column("Mã nhân viên", width=150)
    table.column("Tên nhân viên", width=150)
    table.column("Dữ liệu khuôn mặt", width=150)

    # Hiển thị bảng
    table.pack()

    # Chạy giao diện
    root.mainloop()
