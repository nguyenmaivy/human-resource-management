import tkinter as tk
import DalStaff
from tkinter import messagebox
import DalDepartment
import DalPositionjob
import subprocess
from tkinter import ttk
import traningface
import deleteimg
import DalPhoto
from datetime import datetime

def xoanv():
  
    def manvham(event):
        global manv
        manv = comboboxmanv.get()
        DalStaff.create_connection()  
        tennv = DalStaff.getten(manv)
        name_entry.delete(0, 'end')
        name_entry.insert(0, f"{tennv[0][0]}")
 

    def themthongtin():
      
        name =name_entry.get()
        result = messagebox.askokcancel("Xác nhận", "Xác nhận xóa?")
        if result:
            DalStaff.create_connection()
            temp=DalStaff.delete_employee(comboboxmanv.get())
            messagebox.showinfo("Thông báo ", "Thực hiện thành công!")
            if temp==-1:
                messagebox.askokcancel("Thông báo", "Nhân viên có dữ liệu chấm công không thể xóa")
 
    window = tk.Tk()
    window.title("Ứng dụng chấm công")
    window.geometry("400x300")
    window.configure(bg="lightblue")
    text = tk.Label(window, text="Xóa Thông Tin", bg="lightblue", font=("Arial", 20))
    text.pack()
    manv_label = tk.Label(window, text="Mã nhân viên :", bg="lightblue", font=("Arial", 12))
    manv_label.pack()
    DalStaff.create_connection()
    value = DalStaff.get_idkdk()
    comboboxmanv = ttk.Combobox(window, values=value)
    comboboxmanv.pack()
    comboboxmanv.bind("<<ComboboxSelected>>", manvham)
    name_label = tk.Label(window, text="Tên:", bg="lightblue", font=("Arial", 12))
    name_label.pack()
    name_entry = tk.Entry(window, width=30)
    name_entry.pack()
    clock_in_button = tk.Button(window, text="Xóa Thông Tin", bg="blue", fg="white", font=("Arial", 14),command=themthongtin)
    clock_in_button.pack(pady=20)
    window.mainloop()
