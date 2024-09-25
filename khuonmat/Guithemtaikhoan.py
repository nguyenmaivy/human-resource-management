import tkinter as tk
from tkinter import messagebox
import DalAccount
from tkinter import ttk
selected_value = -1
idselect =-1
def guitk():
    
    def handle_selection(event):
        global selected_value
        selected_value = combobox.get()
    def manhanvien(event):
        global idselect
        idselect = comboboxnv.get()
        


    def deletetk():
        manvien = idselect
        print(manvien)
        DalAccount.create_connection()
        accounts = DalAccount.get_accounts()
        for account in accounts:
            manv = account[1]
            if str(manv) == str(manvien):
                result = messagebox.askokcancel("Xác nhận", "Xác nhận xóa ")
                if result:
                    DalAccount.delete_account(manv)
                    messagebox.showinfo("Thông báo", "Xóa thành công")
                    reset_table()
                    load_data_to_table()
                    # Thực hiện reset lại bảng dữ liệu
                    return

        messagebox.showinfo("Thông báo", "Sai tài khoản")

    def save_position():
        manv = idselect
        mk = entry_mk.get()
        xnmk= entry_mkxn.get()
        pq = selected_value
        print(manv , mk ,pq)
        if manv == "" or mk == "" or pq == -1:
            messagebox.showinfo("Thông báo", "Không để trống")
            return
        if mk !=xnmk:
            messagebox.showinfo("Thông báo", "Không trùng mật khẩu")
            return
        
        DalAccount.create_connection()
        DalAccount.insert_account(manv, mk, pq)
        print("Lưu vị trí công việc")

        reset_table()  

   
        accounts = DalAccount.get_accountmanager()

    
        for account in accounts:
            tree.insert("", tk.END, values=account)

    def reset_table():
        tree.delete(*tree.get_children())
        


    window = tk.Tk()
    window.title("Ứng dụng chấm công")
    window.geometry("300x250")

    label_title = tk.Label(window, text="Quản lý tài khoản", font=("Helvetica", 16, "bold"))
    label_title.pack(pady=10)
    label_manv = tk.Label(window, text="Mã Nhân Viên:")
    label_manv.pack()
    DalAccount.create_connection()
    value = DalAccount.laymanhanvien()
    comboboxnv = ttk.Combobox(window, values=value)
    comboboxnv.pack()
    # Thiết lập sự kiện khi chọn một giá trị
    comboboxnv.bind("<<ComboboxSelected>>", manhanvien)

    # Tạo nhãn "Mật khẩu"
    label_mk = tk.Label(window, text="Mật khẩu:")
    label_mk.pack()
    entry_mk = tk.Entry(window)
    entry_mk.pack()

    label_mkxn = tk.Label(window, text="Xác nhận mật khẩu:")
    label_mkxn.pack()

    entry_mkxn = tk.Entry(window)
    entry_mkxn.pack()
    label_pq = tk.Label(window, text="Phân quyền")
    label_pq.pack()
    combobox = ttk.Combobox(window, values=['o', '1'])
    combobox.pack()
    combobox.bind("<<ComboboxSelected>>", handle_selection)
    button_luu = tk.Button(window, text="Lưu", command=save_position)
    button_luu.pack()
    button_xoa = tk.Button(window, text="Xóa", command=deletetk)
    button_xoa.pack()
    headers = ['Mã nhân viên', 'Họ tên', 'Mật khẩu', 'Phân quyền']

    tree = ttk.Treeview(window, columns=headers, show='headings')
    def load_data_to_table():
        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, width=100)
        DalAccount.create_connection()
        accounts = DalAccount.get_accountmanager()
        for account in accounts:
            tree.insert("", tk.END, values=account)
    tree.pack()
    load_data_to_table()
    window.geometry("500x500")
    window.mainloop()