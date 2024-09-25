import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import testface
def chamcong():
   
    def clock_in():
        name = name_entry.get()
        employee_id = id_entry.get()

        if name and employee_id:
            message = f"Chấm công cho nhân viên:\nTên: {name}\nMã số nhân viên: {employee_id}"
            messagebox.showinfo("Chấm công", message)
            temp= testface.kiemtrakhuonmat(employee_id)
            if(temp==1):
                message = f"Chấm công thành công cho nhân viên:\nTên: {name}\nMã số nhân viên: {employee_id}"
                messagebox.showinfo("Chấm công", message)


        else:
            messagebox.showerror("Lỗi", "Vui lòng nhập tên và mã số nhân viên.")


    
    window = tk.Tk()
    window.title("Ứng dụng chấm công")


    window.geometry("500x300")

   
    name_label = tk.Label(window, text="Tên:")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    id_label = tk.Label(window, text="Mã số nhân viên:")
    id_label.pack()
    id_entry = tk.Entry(window)
    id_entry.pack()

    clock_in_button = tk.Button(window, text="Chấm công", command=clock_in)
    clock_in_button.pack()

    table = ttk.Treeview(window, columns=("STT", "Tên", "Ngày chấm công"), show="headings")
    table.pack()

    table.heading("STT", text="STT")
    table.heading("Tên", text="Tên")
    table.heading("Ngày chấm công", text="Ngày chấm công")

    sample_data = [
        (1, "John Doe", "2022-01-15"),
        (2, "Jane Smith", "2022-01-16"),
        (3, "Bob Johnson", "2022-01-17"),
        (4, "Alice Williams", "2022-01-18"),
        (5, "Mike Brown", "2022-01-19")
    ]

    for data in sample_data:
        table.insert("", "end", values=data)
    window.mainloop()