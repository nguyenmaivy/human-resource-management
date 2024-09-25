import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Dalchamcong
import DalLuong
import DalAccount
from datetime import datetime
def show_table(data):
    def timchamcong():
        manv = comboboxnv.get()
        thang = month_combobox.get()
        data = Dalchamcong.get_nhanvientaithang(manv, thang)
        table.delete(*table.get_children())
        if data is not None:
            for row in data:
                table.insert("", tk.END, values=(row[0], row[1], row[2]))
    def themchamcong():
        manv = comboboxnv.get()
        date =dayxn.get()
        thang = month_combobox.get()
        date_format = "%d/%m/%Y"
        try:
            date_object = datetime.strptime(date, date_format)
            formatted_date = date_object.strftime("%Y-%m-%d")
            month = date_object.strftime("%m").lstrip('0')
            print(month,thang)
   
        except ValueError:
            messagebox.showerror("Lỗi", "Ngày không đúng định dạng!")
            return
        if month!=thang :
             messagebox.showerror("Lỗi", "Sai tháng!")
             return
        Dalchamcong.insert_chamcong1(manv,formatted_date)
        timchamcong()


    root = tk.Tk()
    values = Dalchamcong.get_thangchamcongkdk()

    # Tạo frame chứa các combobox và nút
    selection_frame = tk.Frame(root)
    selection_frame.pack()

    name_label1 = tk.Label(selection_frame, text="Mã nhân viên", font=("Arial", 12))
    name_label1.grid(row=0, column=0)
    DalAccount.create_connection()
    value = DalAccount.laymanhanvien()
    comboboxnv = ttk.Combobox(selection_frame, values=value)
    comboboxnv.set(values[0])
    comboboxnv.grid(row=0, column=1)

    name_label = tk.Label(selection_frame, text="Tháng chấm công", font=("Arial", 12))
    name_label.grid(row=0, column=2)
    month_combobox = ttk.Combobox(selection_frame, values=values)
    month_combobox.set(values[0])
    month_combobox.grid(row=0, column=3)

    buttontim = ttk.Button(selection_frame, text="Tìm thông tin chấm công", command=timchamcong)
    buttontim.grid(row=0, column=4)

    name_labe2 = tk.Label(selection_frame, text="Nhập ngày chấm bù", font=("Arial", 12))
    name_labe2.grid(row=1, column=0)
    dayxn = tk.Entry(selection_frame)
    dayxn.grid(row=1, column=1)

    buttonthem = ttk.Button(selection_frame, text="Thêm chấm công",command=themchamcong)
    buttonthem.grid(row=1, column=2)
    table_frame = tk.Frame(root)
    table_frame.pack()

    table = ttk.Treeview(table_frame)
    table["columns"] = ("MaNhanVien", "HoTen", "NgayChamCong")  # Updated column name

    table.column("MaNhanVien", anchor=tk.CENTER)
    table.column("HoTen", anchor=tk.CENTER)
    table.column("NgayChamCong", anchor=tk.CENTER)  # Updated column name

    table.heading("MaNhanVien", text="Mã Nhân Viên")
    table.heading("HoTen", text="Họ Tên")
    table.heading("NgayChamCong", text="Ngày chấm công")  # Updated column name

    table.pack()

    # Hàm sự kiện cho button

    root.mainloop()


Dalchamcong.create_connection()