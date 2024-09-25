import tkinter as tk
from tkinter import ttk
import DalLuong
import Laysaveid

def on_combobox_selected(event, combobox, label):
    selected_item = combobox.get()
    id=Laysaveid.layid()
    temp=DalLuong.get_luong(id,selected_item)
    label.config(text=f"Lương tháng {selected_item} của bạn là: {temp[0][0]}VND")

def create_gui():
    root = tk.Tk()
    root.geometry("400x150")  
    label1 = tk.Label(root, text="Xem lương", font=("Arial", 20, "bold"))
    label1.pack()
    label2 =tk.Label(root, text=" Chọn tháng ")
    label2.pack()
    id=Laysaveid.layid()
    DalLuong.create_connection()
    value= DalLuong.get_thang(int(id))
    combobox = ttk.Combobox(root, values=value)
    combobox.bind("<<ComboboxSelected>>", lambda event: on_combobox_selected(event, combobox, label))
    combobox.pack()

    label = tk.Label(root, text="Lương",font=("Arial", 10, "bold"))
    label.pack()

    root.mainloop()

