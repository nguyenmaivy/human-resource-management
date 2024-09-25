import tkinter as tk
import GUinvthem
import GUinvxoa
import GuiNvsua
import GuiNvxem
import importexcel
def menunv():
    def button1_clicked():
        GuiNvsua.suanhanvien()
        root.deiconify()
        

    def button2_clicked():
        GUinvxoa.xoanv()

    def button3_clicked():
        GUinvthem.themnhanvien()

    def button4_clicked():
        GuiNvxem.create_table()

    def button5_clicked():
        importexcel.excel()

    root = tk.Tk()
    root.geometry("200x350")
    root.title("MainWindow")

    label = tk.Label(root, text="Quản lý Thân viên", font=("Arial", 12, "bold"))
    label.pack()

   


    button2 = tk.Button(root, text="xóa", width=8, command=button2_clicked)
    button2.place(x=70, y=270)

    button3 = tk.Button(root, text="Sửa", width=8, command=button1_clicked)
    button3.place(x=70, y=210)

    button4 = tk.Button(root, text="Xem", width=8, command=button4_clicked)
    button4.place(x=70, y=20)
    button5 = tk.Button(root, text="Thêm excel", width=8, command=button5_clicked)
    button5.place(x=70, y=150)
    button1 = tk.Button(root, text="Thêm", width=8, command=button3_clicked)
    button1.place(x=70, y=80)

    root.mainloop()
