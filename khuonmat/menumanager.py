from tkinter import messagebox
import menunhanvien
import Guithemtaikhoan
from Guivitricongviec1 import PositionManagementApp
from GuiPhongban1 import DepartmentManagementApp
import trandata
import GUiquanlychamcong
import GUITinhluong
import tkinter as tk
import Guihavefaceid

def manage_info():
    # Code for managing information
    print("Thông tin")
    menunhanvien.menunv()

def manage_attendance():
    # Code for managing attendance
    print("Chấm công")
    GUiquanlychamcong.show_table(None)

def manage_departments():
    # Code for managing departments
    app1 = DepartmentManagementApp()
    # Run the Tkinter event loop
    app1.mainloop()

def manage_job_positions():
    # Code for managing job positions
    print("Ql cv")
    app = PositionManagementApp()
    # Run the Tkinter event loop
    app.mainloop()
def data():
    Guihavefaceid.tinhtrang()
def manage_salary():
    # Code for managing salary
    print("Quản lý lương")
    GUITinhluong.show_table(None)

def manage_accounts():
    print("Quản lý tài khoản")
    Guithemtaikhoan.guitk()

def process_face_data():
    # Code for processing face data
    trandata.training()
    print("Xử lí dữ liệu khuôn mặt")
    # Gọi các hàm hoặc thực hiện các thao tác cần thiết để xử lí dữ liệu khuôn mặt ở đây

def create_ui():
    root = tk.Tk()
    root.title("MainWindow")
    root.geometry("400x600")

    centralwidget = tk.Frame(root)
    centralwidget.pack()

    label = tk.Label(centralwidget, text="Quản lý nhân sự", font=("Arial", 20, "bold"))
    label.pack()

    pushButton_3 = tk.Button(centralwidget, text="Quản lý thông tin", command=manage_info, width=20, height=2)
    pushButton_3.pack(pady=10)

    pushButton_4 = tk.Button(centralwidget, text="Quản lý chấm công", command=manage_attendance, width=20, height=2)
    pushButton_4.pack(pady=10)

    pushButton_5 = tk.Button(centralwidget, text="Quản lý phòng ban", command=manage_departments, width=20, height=2)
    pushButton_5.pack(pady=10)

    pushButton_6 = tk.Button(centralwidget, text="Quản lý vị trí công việc", command=manage_job_positions, width=20, height=2)
    pushButton_6.pack(pady=10)

    pushButton_7 = tk.Button(centralwidget, text="Quản lý lương", command=manage_salary, width=20, height=2)
    pushButton_7.pack(pady=10)

    pushButton_8 = tk.Button(centralwidget, text="Tình trạng cập nhập dữ liệu", command=data, width=20, height=2)
    pushButton_8.pack(pady=10)

    pushButton_9 = tk.Button(centralwidget, text="Quản lý tài khoản", command=manage_accounts, width=20, height=2)
    pushButton_9.pack(pady=10)

    pushButton_face = tk.Button(centralwidget, text="Xử lí khuôn mặt", command=process_face_data, width=20, height=2)
    pushButton_face.pack(pady=10)
    root.mainloop()
