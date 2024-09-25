import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime
import Guixemlschamcong
import Laysaveid
import Guidoimatkhau
import Guixemlschamcong
import Laysaveid
import Guixemluong
import test
import DalPhoto
import Dalchamcong
import DalStaff
import traningface

def record_attendance():
    # Code for recording attendance
    print("chấm công")
    id = Laysaveid.layid()
    print(id)
    ngay = datetime.now().date()

    DalPhoto.create_connection()
    ten = DalPhoto.get_ten(id)
    print(ten)
    result = test.testface(ten)
    if result == 1:
        message = "Chấm công thành công"
        messagebox.showinfo("Chấm công", message)
        Dalchamcong.create_connection()
        Dalchamcong.insert_chamcong1(id, ngay)

def view_attendance_table():
    # Code for viewing attendance table
    print("bang cham cong")
    Guixemlschamcong.create_attendance_window()

def view_salary():
    # Code for viewing salary
    print("luong")
    Guixemluong.create_gui()

def change_password():
    # Code for changing password
    Guidoimatkhau.guidoimk()
def face():
    response = messagebox.askquestion("Thông báo", "Bạn có muốn thêm khuôn mặt?")
    if response == 'yes':
        DalPhoto.create_connection()
        idnv = Laysaveid.layid()
        ten = DalStaff.getten(idnv)
        name=ten[0][0].strip()
        temp=DalPhoto.check_id_exists(idnv)
        if(temp==1):
            messagebox.showinfo("Thông báo", "bạn đẫ có dữ liệu khuôn mặt!") 
        else :
         messagebox.showinfo("Thông báo", "Chờ lấy dữ liệu")
         traningface.takephoto(str(idnv) + name.rsplit(' ', 1)[-1])
         DalPhoto.insert_face_id("", idnv, str(idnv) + name.rsplit(' ', 1)[-1])
         messagebox.showinfo("Thông báo", "Thực hiện thành công!")

def run_application():
    root = tk.Tk()
    root.title("Menu Staff")
    root.geometry("370x270")
    id = Laysaveid.layid()
    label = tk.Label(root, text=f"Mã nhân viên: {id}")
    label.place(x=30, y=0)
    DalStaff.create_connection()
    name = DalStaff.getname(id)
    label1 = tk.Label(root, text=f"Tên nhân viên: {name}")
    label1.place(x=150, y=0)

    idnv = Laysaveid.layid()
    DalPhoto.create_connection()
    temp = DalPhoto.check_id_exists(idnv)
    print(idnv)
    print(temp)
    if temp == 1:
     label2 = tk.Label(root, text=f"Tình trạng: Bạn đã có dữ liệu khuôn mặt", fg="blue")
    else:
     label2 = tk.Label(root, text=f"Tình trạng: Bạn chưa có dữ liệu khuôn mặt", fg="red")
    label2.place(x=30, y=25)

    attendance_button = tk.Button(root, text="Chấm công", command=record_attendance)
    attendance_button.place(x=30, y=50, width=131, height=51)

    attendance_table_button = tk.Button(root, text="Xem bảng chấm công", command=view_attendance_table)
    attendance_table_button.place(x=200, y=50, width=131, height=51)

    salary_button = tk.Button(root, text="Xem lương", command=view_salary)
    salary_button.place(x=30, y=120, width=131, height=51)

    faceid = tk.Button(root, text="Cập nhận khuôn mặt", command=face)
    faceid.place(x=30, y=190, width=131, height=51)

    password_button = tk.Button(root, text="Đổi mật khẩu", command=change_password)
    password_button.place(x=200, y=120, width=131, height=51)

    root.mainloop()
    root.destroy()  # Đảm bảo cửa sổ được đóng đúng cách
