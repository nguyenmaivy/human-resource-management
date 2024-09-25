import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Dalchamcong
import DalLuong

def show_table(data):
    root = tk.Tk()
    values = Dalchamcong.get_thangchamcongkdk()
    month_combobox = ttk.Combobox(root, values=values)
    month_combobox.set(values[0])
    month_combobox.pack()

    table = ttk.Treeview(root)
    table["columns"] = ("MaNhanVien", "HoTen", "ViTriCongViec", "SoNgayChamCong", "HeSoLuong")

    table.column("#0", width=0, stretch=tk.NO)
    table.column("MaNhanVien", anchor=tk.CENTER)
    table.column("HoTen", anchor=tk.CENTER)
    table.column("ViTriCongViec", anchor=tk.CENTER)
    table.column("SoNgayChamCong", anchor=tk.CENTER)
    table.column("HeSoLuong", anchor=tk.CENTER)

    table.heading("MaNhanVien", text="Mã Nhân Viên")
    table.heading("HoTen", text="Họ Tên")
    table.heading("ViTriCongViec", text="Vị Trí Công Việc")
    table.heading("SoNgayChamCong", text="Số Ngày Chấm Công")
    table.heading("HeSoLuong", text="Hệ Số Lương")

    def on_month_selected(event):
        selected_month = month_combobox.get()
        data = Dalchamcong.get_sochamcongtrongthang(int(selected_month))
        table.delete(*table.get_children())
        if data is not None:
            for row in data:
                table.insert("", tk.END, values=row)

    month_combobox.bind("<<ComboboxSelected>>", on_month_selected)

    table.pack()

    def on_button_click():
        selected_month = month_combobox.get()
        messagebox.showinfo("Thông báo",f"Bạn Muốn tính lương cho tháng:{selected_month}")
        result = messagebox.askokcancel("Xác nhận", "Xác nhận tính lương?")
        if result:
            handle_ok_button(selected_month)   
    def handle_ok_button(month):
        data=Dalchamcong.get_sochamcongtrongthang(month)
        DalLuong.create_connection()

        if data is not None:
         for row in data:
            
            ma_nhanvien = row[0]
            ho_ten = row[1]
            vi_tri_congviec = row[2]
            so_ngay_chamcong = row[3]
            he_so_luong = row[4]
            luong=8*so_ngay_chamcong*25000*he_so_luong
            DalLuong.insert(ma_nhanvien,month,luong)
        
    button = ttk.Button(root, text="Tính lương", command=on_button_click)
    button.pack()

    root.mainloop()

Dalchamcong.create_connection()

