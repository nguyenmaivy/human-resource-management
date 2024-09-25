import tkinter as tk
from tkinter import messagebox
import DalAccount
from tkinter import ttk

def guidoimk():
    def save_position():

        manv = entry_manv.get()
        mk = entry_mk.get()
        mknew = entry_mkxn.get()
        DalAccount.create_connection()

        accounts = DalAccount.get_accounts()

        for account in accounts:
            matk=account[0]
            manvien = account[1]  
            mkhau = account[2]  
            pq = account[3]  
            if str(manvien) == str(manv) and str(mkhau)==mk:
                DalAccount.update_account(manv, mknew, pq)
                messagebox.showinfo("Đổi thành công","Đã đổi thành công mật khẩu")   
                return
            
            messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không đúng.")    
            return
   
    window = tk.Tk()
    window.title("Ứng dụng chấm công")

    window.geometry("300x300")

    label_title = tk.Label(window, text="ĐỔi Mật khẩu", font=("Helvetica", 16, "bold"))
    label_title.pack(pady=10)
    label_manv = tk.Label(window, text="Mã Nhân Viên:")
    label_manv.pack()

    entry_manv = tk.Entry(window)
    entry_manv.pack()

    label_mk = tk.Label(window, text="Mật khẩu:")
    label_mk.pack()

    entry_mk = tk.Entry(window)
    entry_mk.pack()

    label_mkxn = tk.Label(window, text="Mật khẩu mới")
    label_mkxn.pack()

    entry_mkxn = tk.Entry(window)
    entry_mkxn.pack()


    # Tạo nút "Lưu"
    button_luu = tk.Button(window, text="Lưu", command=save_position)
    button_luu.pack()

    # Khởi chạy vòng lặp chính của giao diện
    window.mainloop()