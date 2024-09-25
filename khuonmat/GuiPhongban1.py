import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import DalDepartment

class DepartmentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý phòng ban")
        self.geometry("600x300")

        # Left frame for buttons
        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side="left", fill="y")

        # Main buttons
        buttons = [("Sửa thông tin", self.suaPhongBan),
                   ("Thêm phòng ban", self.themPhongBan),
                   ("Xem phòng ban", self.xemPhongBan),
                   ("Xóa phòng ban", self.xoaPhongBan)]

        for text, command in buttons:
            button = tk.Button(self.left_frame, text=text, command=command, width=20)
            button.pack(pady=10, fill="both")

        # Right frame for functionality
        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Call functions to setup frames
        self.setup_sua_frame()
        self.setup_them_frame()
        self.setup_xem_frame()
        self.setup_xoa_frame()

        # Hide all frames initially
        self.hide_all_frames()

        # Populate comboboxes
        self.maPhongBan()

    def setup_sua_frame(self):
        self.sua_frame = tk.Frame(self.right_frame, width=500, height=300)
        self.sua_frame.grid(row=0, column=0, sticky="nsew")

        maPhongBan_label = tk.Label(self.sua_frame, text='Mã phòng ban')
        maPhongBan_label.pack()
        self.comboboxmaPhongBan_sua = ttk.Combobox(self.sua_frame)
        self.comboboxmaPhongBan_sua.pack()
        self.comboboxmaPhongBan_sua.bind("<<ComboboxSelected>>", self.on_combobox_select_sua)

        self.name_label = tk.Label(self.sua_frame, text="Tên phòng ban:")
        self.name_label.pack()
        self.name_entry1 = tk.Entry(self.sua_frame)
        self.name_entry1.pack()

        self.button_luu = tk.Button(self.sua_frame, text="Lưu", command=self.suathongtin)
        self.button_luu.pack()

    def setup_them_frame(self):
        self.them_frame = tk.Frame(self.right_frame, width=500, height=300)
        self.them_frame.grid(row=0, column=0, sticky="nsew")

        label_tenphongban = tk.Label(self.them_frame, text="Tên phòng ban:")
        label_tenphongban.pack()

        self.tenphongban_entry = tk.Entry(self.them_frame)
        self.tenphongban_entry.pack()

        button_luu = tk.Button(self.them_frame, text="Lưu", command=self.save_department)
        button_luu.pack()

    def setup_xem_frame(self):
        self.xem_frame = tk.Frame(self.right_frame, width=500, height=300)
        self.xem_frame.grid(row=0, column=0, sticky="nsew")

        columns = ('MaPhongBan', 'TenPhongBan')
        self.tree = ttk.Treeview(self.xem_frame, columns=columns, show='headings')
        self.tree.grid(row=0, column=0, sticky='nsew')

        self.tree.heading('MaPhongBan', text='Mã phòng ban')
        self.tree.heading('TenPhongBan', text='Tên phòng ban')

    def setup_xoa_frame(self):
        self.xoa_frame = tk.Frame(self.right_frame, width=500, height=300)
        self.xoa_frame.grid(row=0, column=0, sticky="nsew")

        maPhongBan_label = tk.Label(self.xoa_frame, text='Mã phòng ban')
        maPhongBan_label.pack()
        self.comboboxmaPhongBan_xoa = ttk.Combobox(self.xoa_frame)
        self.comboboxmaPhongBan_xoa.pack()
        self.comboboxmaPhongBan_xoa.bind("<<ComboboxSelected>>", self.on_combobox_select_xoa)

        name_label = tk.Label(self.xoa_frame, text="Tên phòng ban:")
        name_label.pack()
        self.name_entry = tk.Entry(self.xoa_frame)
        self.name_entry.pack()

        button_xoa = tk.Button(self.xoa_frame, text="Xóa Thông Tin", command=self.xoathongtin)
        button_xoa.pack()

    def hide_all_frames(self):
        frames = [self.sua_frame, self.them_frame, self.xem_frame, self.xoa_frame]
        for frame in frames:
            frame.grid_forget()

    def suaPhongBan(self):
        self.hide_all_frames()
        self.sua_frame.grid(row=0, column=0, sticky="nsew")
        self.on_combobox_select_sua()  # Gọi hàm để cập nhật thông tin từ combobox

    def themPhongBan(self):
        self.hide_all_frames()
        self.them_frame.grid(row=0, column=0, sticky="nsew")

    def xemPhongBan(self):
        self.hide_all_frames()
        self.xem_frame.grid(row=0, column=0, sticky="nsew")
        self.update_xem_frame_data()  # Gọi hàm cập nhật dữ liệu khi chuyển sang khung xem

    def xoaPhongBan(self):
        self.hide_all_frames()
        self.xoa_frame.grid(row=0, column=0, sticky="nsew")

    def maPhongBan(self, event=None):
        DalDepartment.create_connection()
        data = DalDepartment.get_mapb()
        self.comboboxmaPhongBan_xoa['values'] = data  # Populate combobox for delete
        self.comboboxmaPhongBan_sua['values'] = data  # Populate combobox for edit
        if data:
            self.comboboxmaPhongBan_xoa.set(data[0])  # Set the first item as default
            self.comboboxmaPhongBan_sua.set(data[0])  # Set the first item as default
            self.on_combobox_select_xoa()  # Call the function to update other fields

    def on_combobox_select_xoa(self, event=None):
        maPhongBan = self.comboboxmaPhongBan_xoa.get()
        DalDepartment.create_connection()
        tenpb = DalDepartment.get_tenpb(maPhongBan)
        self.name_entry.delete(0, 'end')
        self.name_entry.insert(0, tenpb[0][0])

    def on_combobox_select_sua(self, event=None):
        maPhongBan = self.comboboxmaPhongBan_sua.get()
        DalDepartment.create_connection()
        tenpb = DalDepartment.get_tenpb(maPhongBan)
        self.name_entry1.delete(0, 'end')
        self.name_entry1.insert(0, tenpb[0][0])

    def suathongtin(self):
        tenpb = self.name_entry1.get()

        if not (self.comboboxmaPhongBan_sua.get() and tenpb):
            messagebox.showinfo("Thông báo", "Không để trống")
            return
        else:
            DalDepartment.create_connection()
            DalDepartment.update_department(self.comboboxmaPhongBan_sua.get(), tenpb)
            messagebox.showinfo("Thông báo", "Sửa thông tin phòng ban thành công")
            self.hide_all_frames()
            self.maPhongBan()  # Cập nhật lại dữ liệu cho combobox
            self.update_xem_frame_data()  # Cập nhật dữ liệu trong khung xem

    def save_department(self):
        tenpb = self.tenphongban_entry.get()

        if not tenpb:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        else:
            DalDepartment.create_connection()
            DalDepartment.insert_department(tenpb)
            messagebox.showinfo("Thông báo", "Thêm phòng ban thành công")
            self.hide_all_frames()
            self.maPhongBan()  # Cập nhật lại dữ liệu cho combobox
            self.update_xem_frame_data()  # Cập nhật dữ liệu trong khung xem

    def xoathongtin(self):
        result = messagebox.askokcancel("Xác nhận", "Xác nhận xóa?")
        if result:
            DalDepartment.create_connection()
            temp = DalDepartment.delete_department(self.comboboxmaPhongBan_xoa.get())
            if temp == -1:
                messagebox.askokcancel("Thông báo", "Không thể xóa phòng ban. Vẫn còn nhân viên làm việc ở phòng ban này.")
            self.hide_all_frames()
            self.maPhongBan()  # Cập nhật lại dữ liệu cho combobox
            self.update_xem_frame_data()  # Cập nhật dữ liệu trong khung xem

    def update_xem_frame_data(self):
        self.tree.delete(*self.tree.get_children())  # Clear existing data

        DalDepartment.create_connection()
        data = DalDepartment.get_all_department()

        for row in data:
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    app = DepartmentManagementApp()
    app.mainloop()
