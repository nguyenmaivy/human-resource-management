import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import DalAccount
import MenuStaff
from PyQt6 import QtWidgets
import menumanager
# from MenuStaff import Ui_MainWindow1
import MenuStaff
import os
import deletesaveid
import datetime
import threading

def onloggin():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        connection = DalAccount.create_connection()
        accounts = DalAccount.get_accounts()

        for account in accounts:
            matk = account[0]
            manv = account[1] 
            mk = account[2] 
            pq = account[3] 

            if str(username) == str(manv) and str(password) == str(mk):
                messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
                print(pq)
                window.withdraw()
                if pq == 0:
                    deletesaveid.delete()
                    path = 'pydoan/khuonmat/saveid'
                    new_filename = f'{username}.txt'
                    new_file_path = os.path.join(path, new_filename)
                    open(new_file_path, 'a').close()
                    print("Đã thêm file mới thành công!")
                    MenuStaff.run_application()
                    window.deiconify()
                
                elif pq == 1:
                    deletesaveid.delete()
                    path = 'pydoan/khuonmat/saveid'
                    new_filename = f'{username}.txt'
                    new_file_path = os.path.join(path, new_filename)
                    open(new_file_path, 'a').close()
                    print("Đã thêm file mới thành công!")
                    menumanager.create_ui()
                    window.deiconify()
                

        messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng.")

    window = tk.Tk()
    window.title("Đăng nhập")
    window.geometry("700x400")
    window.configure(bg="lightblue")

    background = tk.Label(window, bg="lightblue")
    background.place(relwidth=1, relheight=1)

    loggin_label = tk.Label(window, text="Loggin", bg="lightblue", fg="white", font=("Arial", 20, "bold"))
    loggin_label.place(relx=0.6, rely=0.2)
    username_label = tk.Label(window, text="Tài khoản ", bg="lightblue", fg="white", font=("Arial", 10, "bold"))
    username_label.place(relx=0.6, rely=0.3)

    username_entry = tk.Entry(window)
    username_entry.place(relx=0.7, rely=0.3)

    password_label = tk.Label(window, text="Mật khẩu ", bg="lightblue", fg="white", font=("Arial", 10, "bold"))
    password_label.place(relx=0.6, rely=0.4)

    password_entry = tk.Entry(window, show="*")
    password_entry.place(relx=0.7, rely=0.4)

    login_button = tk.Button(window, text="Đăng nhập", command=login, bg="white", fg="lightblue")
    login_button.place(relx=0.7, rely=0.5)

    logo_path =  'pydoan/logo.jpg'
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((400, 400))  
    logo_photo = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(window, image=logo_photo)
    logo_label.place(relx=0, rely=0)

    window.mainloop()

def run_login():
    thread = threading.Thread(target=onloggin)
    thread.start()

run_login()