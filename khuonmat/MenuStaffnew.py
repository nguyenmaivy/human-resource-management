from tkinter import *
from PIL import Image, ImageTk
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
    global root
    root = tk.Tk()
    root.title("Menu Staff")
    root.geometry("850x600")
    root.configure(bg="#5f7ddb")
    # Chia cửa sổ thành hai cột
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    # Cấu hình trọng số cho cột chứa các chức năng
    # root.columnconfigure(0, weight=1)
    
    id = Laysaveid.layid()
    # icon1 = ImageTk.PhotoImage(Image.open("khuonmat/icon/identification.png").resize((40,40), resample=Image.LANCZOS))
    # icon2 = ImageTk.PhotoImage(Image.open("khuonmat/icon/id-card.png").resize((40,40), resample=Image.LANCZOS))
    # icon3 = ImageTk.PhotoImage(Image.open("khuonmat/icon/terms-and-conditions.png").resize((40,40), resample=Image.LANCZOS))

    label = tk.Label(root, text=f"Mã nhân viên: {id}", bg="#5f7ddb", fg='white',font = ("Arial", 14, "bold"),compound='left',padx=5)
    label.grid(sticky=NW, row=0, column=0, padx=5, pady=5)
    
    DalStaff.create_connection()
    name = DalStaff.getname(id)
    label1 = tk.Label(root, text=f"Tên nhân viên: {name}", bg="#5f7ddb", fg='white', font = ("Arial", 14, "bold"), compound='left',padx=5)
    label1.place(x=5,y=35)

    idnv = Laysaveid.layid()
    DalPhoto.create_connection()
    temp = DalPhoto.check_id_exists(idnv)
    print(idnv)
    print(temp)
    if temp == 1:
        label2 = tk.Label(root, text=f"Tình trạng: Bạn đã có dữ liệu khuôn mặt", fg="blue", bg="#5f7ddb", compound='left',padx=5)
    else:
        label2 = tk.Label(root, text=f"Tình trạng: Bạn chưa có dữ liệu khuôn mặt", fg="red", bg="#5f7ddb", image=icon3, compound='left',padx=5)
    label2.place(x=5, y=80)

    min_w = 400
    max_w = 400
    cur_width = min_w
    expanded = False
    

    def expand():
        nonlocal cur_width, expanded
        cur_width += 10
        rep = root.after(5,expand)
        frame.config(width=cur_width)
        if cur_width >= max_w:
            expanded = True
            root.after_cancel(rep)
            fill()

    def contract():
        
        nonlocal cur_width, expanded
        cur_width -= 10
        rep = root.after(5,contract)
        frame.config(width=cur_width)
        if cur_width <= min_w:
            expanded = False
            root.after_cancel(rep)
            fill()


    def fill():
        if expanded:
            attendance_button.config(text='Chấm công', image=timekeeping, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            attendance_table_button.config(text='Xem bảng chấm công', image=timesheets, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            salary_button.config(text='Xem lương', image=salary, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            faceid.config(text='Cập nhật khuôn mặt', image=aspect, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            password_button.config(text='Đổi mật khẩu', image=passw, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
        else:
            attendance_button.config(text='Chấm công', image=timekeeping, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            attendance_table_button.config(text='Xem bảng chấm công', image=timesheets, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            salary_button.config(text='Xem lương', image=salary, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            faceid.config(text='Cập nhật khuôn mặt', image=aspect, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            password_button.config(text='Đổi mật khẩu', image=passw, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)


    timekeeping = ImageTk.PhotoImage(Image.open('khuonmat/icon/cham_cong.png').resize((40,40), Image.LANCZOS))
    timesheets = ImageTk.PhotoImage(Image.open('khuonmat/icon/xem_cham_cong.png').resize((40,40), Image.LANCZOS))
    salary = ImageTk.PhotoImage(Image.open('khuonmat/icon/xem_luong.png').resize((40,40), Image.LANCZOS))
    on_hover_image = ImageTk.PhotoImage(Image.open('logo.jpg').resize((400,600), Image.LANCZOS))  # Chỉnh kích thước logo
    aspect = ImageTk.PhotoImage(Image.open('khuonmat/icon/khuon_mat.png').resize((40,40), Image.LANCZOS))  # Chỉnh kích thước logo
    passw = ImageTk.PhotoImage(Image.open('khuonmat/icon/password.png').resize((40,40), Image.LANCZOS))  # Chỉnh kích thước logo

    # Cập nhật chiều rộng
    root.update()
    frame = Frame(root,bg='#5f7ddb',width=100,height=root.winfo_height())
    frame.place(x=5, y=120)

    # Tạo các nút hiển thị
    # imge1_button = Label(root, image=icon1,bg='#5f7đb' )
    attendance_button = Button(frame,image=timekeeping,bg='#5f7ddb',relief='flat', command=record_attendance)
    attendance_table_button = Button(frame,image=timesheets,bg='#5f7ddb',relief='flat',command=view_attendance_table)
    salary_button = Button(frame,image=salary,bg='#5f7ddb',relief='flat', command=view_salary)
    faceid= Button(frame,image=aspect,bg='#5f7ddb',relief='flat', command=face)
    password_button = Button(frame,image=passw,bg='#5f7ddb',relief='flat', command=change_password)

    # Đặt chúng trên frame
    # imge1_button.grid(row=0, column=0, sticky=W, padx=2, pady=4)
    attendance_button.grid(row=0,column=0,sticky=W, padx=2, pady=4)
    attendance_table_button.grid(row=1,column=0,sticky=W, padx=2, pady=4)
    salary_button.grid(row=2,column=0, sticky=W, padx=2, pady=4)
    faceid.grid(row=3,column=0, sticky=W, padx=2, pady=4)
    password_button.grid(row=4,column=0, sticky=W, padx=2, pady=4)
    
    # Khởi tạo label để chứa hình ảnh logo
    hover_image_label = Label(root, image=on_hover_image, bg='white')
    hover_image_label.grid(row=0, column=1, sticky=E)

    # Liên kết với frame, nếu đã nhập hoặc để lại
    frame.bind('<Enter>',lambda e: expand())
    frame.bind('<Leave>',lambda e: contract())
    frame.grid_propagate(False)
    root.mainloop()

run_application()
