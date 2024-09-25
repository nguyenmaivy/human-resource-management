import tkinter as tk
from tkinter import ttk
from mysql.connector import connect, Error
import sys
import threading
import Dalchamcong
import Laysaveid

class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bảng chấm công")
        self.geometry("400x300")

  
        self.combobox = ttk.Combobox(self)
        self.combobox.pack(pady=10, padx=10)

        id = Laysaveid.layid()
        try:
            Dalchamcong.create_connection()
            data = Dalchamcong.get_chamcong(id, 3)
            self.combobox['values'] = Dalchamcong.get_thangchamcong(id)

        
            self.combobox.bind("<<ComboboxSelected>>", self.on_combobox_selected)

            # Tạo bảng
            self.table = ttk.Treeview(self)
            self.table["columns"] = ("Tên nhân viên", "Ngày chấm công")
            self.table.heading("#0", text="STT", anchor=tk.W)
            self.table.heading("Tên nhân viên", text="Mã nhân viên", anchor=tk.W)
            self.table.heading("Ngày chấm công", text="Ngày chấm công", anchor=tk.W)
            self.table.column("#0", width=40)
            self.table.column("Tên nhân viên", width=150)
            self.table.column("Ngày chấm công", width=150)
            self.table.pack(pady=10, padx=10)

            self.display_data(data)
        except Error as e:
            print("Lỗi khi kết nối cơ sở dữ liệu:", e)

    def on_combobox_selected(self, event):
        selected_value = self.combobox.get()

        self.clear_data()

        id = Laysaveid.layid()
        data = Dalchamcong.get_chamcong(id, selected_value)
        self.display_data(data)

    def display_data(self, data):
        for i, (ten_nhan_vien, ngay_cham_cong) in enumerate(data, start=1):
            self.table.insert("", tk.END, text=str(i), values=(ten_nhan_vien, ngay_cham_cong.strftime('%Y-%m-%d')))

    def clear_data(self):
        self.table.delete(*self.table.get_children())

def create_attendance_window():
    window = MyWindow()
    window.mainloop()