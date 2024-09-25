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
vtcv = -1
mapb =-1
gt=""
manv=-1
def suanhanvien():
    
    def manvham(event):
        global manv
        manv = comboboxmanv.get()
        DalStaff.create_connection() 
        tennv = DalStaff.getten(manv)
        name_entry.delete(0, 'end')  
        name_entry.insert(0, f"{tennv[0][0]}")
    def ingt(event):
        global gt
        gt = comboboxsex.get()

    def mavtcv(event):
        global vtcv
        vtcv = combobox.get()
        DalPositionjob.create_connection()
        ten = DalPositionjob.get_tencv(vtcv)
        positionjob_label.config(text=f"Vị trí công việc: {ten[0][0]}")


    def mapban(event):
        global mapb
        mapb = comboboxnv.get()
        DalDepartment.create_connection()
        tenpb = DalDepartment.get_tenpb(mapb)
        department_label.config(text=f"Vị trí công việc: {tenpb[0][0]}")

    def run_takephoto():

        subprocess.run(['python', 'BUS/takephoto.py'])

    def themthongtin():
        name =name_entry.get()
        address = dc_entry.get()
        cm =cm_entry.get()

        date = date_entry.get()
        date_format = "%d/%m/%Y"
        try:
            date_object = datetime.strptime(date, date_format)
            formatted_date = date_object.strftime("%Y-%m-%d")
            # Tiếp tục xử lý các thao tác khác sau khi nhận được ngày đúng định dạng
        except ValueError:
            messagebox.showerror("Lỗi", "Ngày không đúng định dạng!")
            return
        if id == '' or name == '' or address == '' or date == '' or cm == '':
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return
        else:
            DalStaff.create_connection()
            DalStaff.update_employee(comboboxmanv.get(),name,formatted_date,comboboxsex.get(), cm,address,combobox.get(),comboboxnv.get())
            messagebox.showinfo("Thông báo", "Thực hiện thành công!")
            DalStaff.close_connection()
        
    window = tk.Tk()
    window.title("Ứng dụng chấm công")
    window.geometry("500x500")
    text = tk.Label(window, text="Sửa thông tin",   font=("Arial", 20))
    text.pack()


    manv_label = tk.Label(window, text="Mã nhân viên :",   font=("Arial", 12))
    manv_label.pack()
    DalStaff.create_connection()
    value = DalStaff.get_idkdk()
    comboboxmanv = ttk.Combobox(window, values=value)
    comboboxmanv.pack()
    comboboxmanv.bind("<<ComboboxSelected>>", manvham)

    name_label = tk.Label(window, text="Tên:",   font=("Arial", 12))
    name_label.pack()
    name_entry = tk.Entry(window, width=30)
    name_entry.pack()

    dc_label = tk.Label(window, text="Địa chỉ :",   font=("Arial", 12))
    dc_label.pack()
    dc_entry = tk.Entry(window, width=30)
    dc_entry.pack()

    date_label = tk.Label(window, text="Ngày sinh:",   font=("Arial", 12))
    date_label.pack()
    date_entry = tk.Entry(window, width=30)
    date_entry.pack()

    cm_label = tk.Label(window, text="Số Căng cước:",   font=("Arial", 12))
    cm_label.pack()
    cm_entry = tk.Entry(window, width=30)
    cm_entry.pack()

    sex_label = tk.Label(window, text="Giới tính :",   font=("Arial", 12))
    sex_label.pack()
    value = ["Nam", "Nữ", "Khác"]
    comboboxsex = ttk.Combobox(window, values=value)
    comboboxsex.pack()
    comboboxsex.bind("<<ComboboxSelected>>", ingt)

    positionjob_label = tk.Label(window, text="Vị trí công việc :",   font=("Arial", 12))
    positionjob_label.pack()
    DalPositionjob.create_connection()
    value = DalPositionjob.get_macv1()
    combobox = ttk.Combobox(window, values=value)
    combobox.pack()
    combobox.bind("<<ComboboxSelected>>", mavtcv)

    department_label = tk.Label(window, text=" Phòng ban :",   font=("Arial", 12))
    department_label.pack()
    DalDepartment.create_connection()
    value = DalDepartment.get_mapb()
    comboboxnv = ttk.Combobox(window, values=value)
    comboboxnv.pack()
    comboboxnv.bind("<<ComboboxSelected>>", mapban)
    clock_in_button = tk.Button(window, text="Sửa thông tin", bg="blue", fg="white", font=("Arial", 14),command=themthongtin)
    clock_in_button.pack(pady=20)
    window.mainloop()
