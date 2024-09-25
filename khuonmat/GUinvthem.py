import datetime
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
def themnhanvien():
   
    def ingt(event):
        global gt
        gt = combobox.get()

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

    def themthongtinall():
        name =name_entry.get()
        address = dc_entry.get()
        date = date_entry.get()
        date_format = "%d/%m/%Y"
        
        try:
            date_object = datetime.strptime(date, date_format)
            formatted_date = date_object.strftime("%Y-%m-%d")
    
        except ValueError:
            messagebox.showerror("Lỗi", "Ngày không đúng định dạng!")
            return
        cm =cm_entry.get()
        gtinh= gt
        vitri=vtcv 
        pban = mapb
        
        if id == '' or name == '' or address == '' or date == '' or cm == '':
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return
        else:
            DalStaff.create_connection()
            temp=DalStaff.insert_employee(name,formatted_date,gtinh, cm,address,vitri,pban)
            if temp==0:
                messagebox.showerror("Lỗi", "Nhân viên đã tồn")
            employee_id=DalStaff.get_idnv(name,cm)
            idnv=employee_id[0][0]
            traningface.takephoto(str(idnv)+name.rsplit(' ', 1)[-1])
            DalPhoto.create_connection()
            DalPhoto.insert_face_id("",idnv,str(idnv)+name.rsplit(' ', 1)[-1])
            messagebox.showinfo("Thông báo ", "Thực hiện thành công!")
    def themthongtin():
        name =name_entry.get()
        address = dc_entry.get()
        date = date_entry.get()
        date_format = "%d/%m/%Y"
        
        try:
            date_object = datetime.strptime(date, date_format)
            formatted_date = date_object.strftime("%Y-%m-%d")
    
        except ValueError:
            messagebox.showerror("Lỗi", "Ngày không đúng định dạng!")
            return
        cm =cm_entry.get()
        gtinh= gt
        vitri=vtcv 
        pban = mapb
        
        if id == '' or name == '' or address == '' or date == '' or cm == '':
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
            return
        else:
            DalStaff.create_connection()
            temp=DalStaff.insert_employee(name,formatted_date,gtinh, cm,address,vitri,pban)
            if temp==0:
                messagebox.showerror("Lỗi", "Nhân viên đã tồn")
            # employee_id=DalStaff.get_idnv(name,cm)
            # idnv=employee_id[0][0]
            # traningface.takephoto(str(idnv)+name.rsplit(' ', 1)[-1])
            # DalPhoto.create_connection()
            # DalPhoto.insert_face_id("",idnv,str(idnv)+name.rsplit(' ', 1)[-1])
            # messagebox.showinfo("Thông báo ", "Thực hiện thành công!")

    window = tk.Tk()
    window.title("Ứng dụng chấm công")
    window.geometry("500x500")
    text = tk.Label(window, text="Thêm thông tin",   font=("Arial", 20))
    text.pack()

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
   
    clock_in_button = tk.Button(window, text="Thêm thông tin", bg="blue", fg="white", font=("Arial", 14),command=themthongtin)
    clock_in_button.pack(pady=20)

    clock_in_button1 = tk.Button(window, text="Thêm thông tin có khuôn mặt ", bg="blue", fg="white", font=("Arial", 14),command=themthongtinall)
    clock_in_button1.pack(pady=20)
    window.mainloop()