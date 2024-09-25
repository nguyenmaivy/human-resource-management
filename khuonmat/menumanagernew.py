from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import menunhanvien
import Guithemtaikhoan
import menuphongban
import menucv
import trandata
import GUiquanlychamcong
import GUITinhluong
import Guivitricongviec
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
    menuphongban.run_application()

def manage_job_positions():
    # Code for managing job positions
    print("Ql cv")
    menucv.run_application()
    
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
    trandata.trainingdata()
    print("Xử lí dữ liệu khuôn mặt")
    # Gọi các hàm hoặc thực hiện các thao tác cần thiết để xử lí dữ liệu khuôn mặt ở đây

def create_ui():
    global root
    root = tk.Tk()
    root.title("MainWindow")
    root.geometry("850x600")
    root.configure(bg="#5f7ddb")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)


    # centralwidget = tk.Frame(root)
    # centralwidget.grid(row=0, column=0, sticky=N+W, padx=5, pady=5)


    label = tk.Label(root, text="Quản lý nhân sự",bg="#5f7ddb", fg='white', font=("Arial", 14, "bold"))
    label.grid(sticky=tk.NW, row=0, column=0, padx=7, pady=7)

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
            pushButton_3.config(text="Quản lý thông tin", image=information, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            pushButton_4.config(text="Quản lý chấm công", image=timekeeping, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            pushButton_5.config(text="Quản lý phòng ban", image=departments, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            pushButton_6.config(text="Quản lý vị trí công việc", image=job_position, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            pushButton_7.config(text="Quản lý lương", image=salary, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            pushButton_8.config(text="Tình trạng cập nhập dữ liệu", image=data_update, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            pushButton_9.config(text="Thêm tài khoản", image=add_account, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            pushButton_face.config( text="Xử lí khuôn mặt", image=face_processing, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
        else:
            pushButton_3.config(text="Quản lý thông tin", image=information, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            pushButton_4.config(text="Quản lý chấm công", image=timekeeping, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            pushButton_5.config(text="Quản lý phòng ban", image=departments, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            pushButton_6.config(text="Quản lý vị trí công việc", image=job_position, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            pushButton_7.config(text="Quản lý lương", image=salary, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)
            pushButton_8.config(text="Tình trạng cập nhập dữ liệu", image=data_update, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            pushButton_9.config(text="Thêm tài khoản", image=add_account, font=("Arial", 14, "bold"), compound='left', fg='white', padx=5)
            pushButton_face.config( text="Xử lí khuôn mặt", image=face_processing, font=("Arial", 14, "bold"), compound='left', fg="white", padx=5)

    information = ImageTk.PhotoImage(Image.open('khuonmat/icon/ql_thong_tin.png').resize((40,40), Image.LANCZOS))
    timekeeping = ImageTk.PhotoImage(Image.open('khuonmat/icon/ql_cham_cong.png').resize((40,40), Image.LANCZOS))
    departments = ImageTk.PhotoImage(Image.open('khuonmat/icon/ql_phongban.png').resize((40,40), Image.LANCZOS))
    on_hover_image = ImageTk.PhotoImage(Image.open('logo.jpg').resize((400,600), Image.LANCZOS))  # Chỉnh kích thước logo
    job_position = ImageTk.PhotoImage(Image.open('khuonmat/icon/ql_vitricongviec.png').resize((40,40), Image.LANCZOS))  # Chỉnh kích thước logo
    salary = ImageTk.PhotoImage(Image.open('khuonmat/icon/ql_luong.png').resize((40,40), Image.LANCZOS))  # Chỉnh kích thước logo
    data_update = ImageTk.PhotoImage(Image.open('khuonmat/icon/capnhatdulieu.png').resize((40,40), Image.LANCZOS))
    add_account = ImageTk.PhotoImage(Image.open('khuonmat/icon/them_taikhoan.png').resize((40,40), Image.LANCZOS))
    face_processing = ImageTk.PhotoImage(Image.open('khuonmat/icon/xulikhuonmat.png').resize((40,40), Image.LANCZOS))
    # Cập nhật chiều rộng
    root.update()
    frame = Frame(root,bg='#5f7ddb',width=100,height=root.winfo_height())
    frame.place(x=5, y=40)

    # pushButton_3 = tk.Button(centralwidget, text="Quản lý thông tin", command=manage_info, width=20, height=2)
    # pushButton_3.pack(pady=10)

    # pushButton_4 = tk.Button(centralwidget, text="Quản lý chấm công", command=manage_attendance, width=20, height=2)
    # pushButton_4.pack(pady=10)

    # pushButton_5 = tk.Button(centralwidget, text="Quản lý phòng ban", command=manage_departments, width=20, height=2)
    # pushButton_5.pack(pady=10)

    # pushButton_6 = tk.Button(centralwidget, text="Quản lý vị trí công việc", command=manage_job_positions, width=20, height=2)
    # pushButton_6.pack(pady=10)

    # pushButton_7 = tk.Button(centralwidget, text="Quản lý lương", command=manage_salary, width=20, height=2)
    # pushButton_7.pack(pady=10)

    # pushButton_8 = tk.Button(centralwidget, text="Tình trạng cập nhập dữ liệu", command=data, width=20, height=2)
    # pushButton_8.pack(pady=10)

    # pushButton_9 = tk.Button(centralwidget, text="Thêm tài khoản", command=manage_accounts, width=20, height=2)
    # pushButton_9.pack(pady=10)

    # pushButton_face = tk.Button(centralwidget, text="Xử lí khuôn mặt", command=process_face_data, width=20, height=2)
    # pushButton_face.pack(pady=10)
    # root.mainloop()
    pushButton_3 = Button(frame,image=information,bg='#5f7ddb',relief='flat', command=manage_info)
    pushButton_4 = Button(frame,image=timekeeping,bg='#5f7ddb',relief='flat', command=manage_attendance)
    pushButton_5 = Button(frame,image=departments,bg='#5f7ddb',relief='flat',  command=manage_departments)
    pushButton_6= Button(frame,image=job_position,bg='#5f7ddb',relief='flat', command=manage_job_positions)
    pushButton_7 = Button(frame,image=salary,bg='#5f7ddb',relief='flat', command=manage_salary)
    pushButton_8 = Button(frame,image=data_update,bg='#5f7ddb',relief='flat', command=data)
    pushButton_9 = Button(frame,image=add_account,bg='#5f7ddb',relief='flat',command=manage_accounts)
    pushButton_face = Button(frame,image=face_processing,bg='#5f7ddb',relief='flat',  command=process_face_data)

    # Đặt chúng trên frame
    # imge1_button.grid(row=0, column=0, sticky=W, padx=2, pady=4)
    pushButton_3.grid(row=0,column=0,sticky=W, padx=2, pady=4)
    pushButton_4.grid(row=1,column=0,sticky=W, padx=2, pady=4)
    pushButton_5.grid(row=2,column=0, sticky=W, padx=2, pady=4)
    pushButton_6.grid(row=3,column=0, sticky=W, padx=2, pady=4)
    pushButton_7.grid(row=4,column=0, sticky=W, padx=2, pady=4)
    pushButton_8.grid(row=5,column=0,sticky=W, padx=2, pady=4)
    pushButton_9.grid(row=6,column=0,sticky=W, padx=2, pady=4)
    pushButton_face.grid(row=7,column=0, sticky=W, padx=2, pady=4)
    
    # Khởi tạo label để chứa hình ảnh logo
    hover_image_label = Label(root, image=on_hover_image, bg='white')
    hover_image_label.grid(row=0, column=1, sticky=E)

    # Liên kết với frame, nếu đã nhập hoặc để lại
    frame.bind('<Enter>',lambda e: expand())
    frame.bind('<Leave>',lambda e: contract())
    frame.grid_propagate(False)
    root.mainloop()

create_ui()
