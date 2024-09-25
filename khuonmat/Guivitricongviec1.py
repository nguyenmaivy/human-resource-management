import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import DalPositionjob

class PositionManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý vị trí công việc")
        self.geometry("800x300")

        # Left frame for buttons
        self.left_frame = tk.Frame(self)
        self.left_frame.pack(side="left", fill="y")

        # Main buttons
        buttons = [("Sửa thông tin", self.suaViTriCongViec),
                   ("Thêm vị trí công việc", self.themvtcv),
                   ("Xem vị trí công việc", self.xemvtcv),
                   ("Xóa vị trí công việc", self.xoavtcv)]

        for text, command in buttons:
            button = tk.Button(self.left_frame, text=text, command=command, width=20)
            button.pack(pady=5, padx=10, fill="both", expand=True)

        # Right frame for functionality
        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Call functions to setup frames
        self.setup_sua_frame()
        self.setup_them_frame()
        self.setup_xem_frame()
        self.setup_xoa_frame()

        # Hide all frames initially
        self.right_frame.grid_forget()
        
        # Populate comboboxes
        self.maCV()

    def setup_sua_frame(self):
        self.sua_frame = tk.Frame(self.right_frame, width=500, height=300)
        self.sua_frame.grid(row=0, column=0, sticky="nsew")

        maCV_label = tk.Label(self.sua_frame, text='Mã vị trí công việc')
        maCV_label.pack()
        self.comboboxmaCV_sua = ttk.Combobox(self.sua_frame)
        self.comboboxmaCV_sua.pack()
        self.comboboxmaCV_sua.bind("<<ComboboxSelected>>", self.on_combobox_select_sua)

        self.name_label = tk.Label(self.sua_frame, text="Tên Vị trí công việc:")
        self.name_label.pack()
        self.name_entry1 = tk.Entry(self.sua_frame)
        self.name_entry1.pack()

        self.hesoluong_label = tk.Label(self.sua_frame, text="Hệ số lương:")
        self.hesoluong_label.pack()
        self.hesoluong_entry1 = tk.Entry(self.sua_frame)
        self.hesoluong_entry1.pack()

        self.button_luu = tk.Button(self.sua_frame, text="Lưu", command=self.suathongtin)
        self.button_luu.pack()

    def setup_them_frame(self):
        self.them_frame = tk.Frame(self.right_frame, width=500, height=300)
        self.them_frame.grid(row=0, column=0, sticky="nsew")

        label_tencv = tk.Label(self.them_frame, text="Tên vị trí công việc:")
        label_tencv.pack()

        self.tencv_entry = tk.Entry(self.them_frame)
        self.tencv_entry.pack()

        hesoluong_label = tk.Label(self.them_frame, text="Hệ số lương:")
        hesoluong_label.pack()

        self.hesoluong_entry = tk.Entry(self.them_frame)
        self.hesoluong_entry.pack()

        button_luu = tk.Button(self.them_frame, text="Lưu", command=self.save_department)
        button_luu.pack()

    def setup_xem_frame(self):
        self.xem_frame = tk.Frame(self.right_frame, width=500, height=300)
        self.xem_frame.grid(row=0, column=0, sticky="nsew")

        columns = ('MaViTriCongViec', 'TenViTriCongViec', 'HeSoLuong')
        self.tree = ttk.Treeview(self.xem_frame, columns=columns, show='headings')
        self.tree.grid(row=0, column=0, sticky='nsew')

        self.tree.heading('MaViTriCongViec', text='Mã vị trí công việc')
        self.tree.heading('TenViTriCongViec', text='Tên vị trí công việc')
        self.tree.heading('HeSoLuong', text='Hệ số lương')

        self.update_xem_frame_data()

    def setup_xoa_frame(self):
        self.xoa_frame = tk.Frame(self.right_frame, width=500, height=300)
        self.xoa_frame.grid(row=0, column=0, sticky="nsew")

        maCV_label = tk.Label(self.xoa_frame, text='Mã vị trí công việc')
        maCV_label.pack()
        self.comboboxmaCV_xoa = ttk.Combobox(self.xoa_frame)
        self.comboboxmaCV_xoa.pack()
        self.comboboxmaCV_xoa.bind("<<ComboboxSelected>>", self.on_combobox_select)

        name_label = tk.Label(self.xoa_frame, text="Tên vị trí công việc:")
        name_label.pack()
        self.name_entry = tk.Entry(self.xoa_frame)
        self.name_entry.pack()

        button_xoa = tk.Button(self.xoa_frame, text="Xóa Thông Tin", command=self.xoathongtin)
        button_xoa.pack()

    def suaViTriCongViec(self):
        self.sua_frame.grid(row=0, column=0, sticky="nsew")
        self.them_frame.grid_forget()
        self.xem_frame.grid_forget()
        self.xoa_frame.grid_forget()
        self.on_combobox_select_sua()  # Gọi hàm để cập nhật thông tin từ combobox

    def themvtcv(self):
        self.sua_frame.grid_forget()
        self.them_frame.grid(row=0, column=0, sticky="nsew")
        self.xem_frame.grid_forget()
        self.xoa_frame.grid_forget()

    def xemvtcv(self):
        self.sua_frame.grid_forget()
        self.them_frame.grid_forget()
        self.xem_frame.grid(row=0, column=0, sticky="nsew")
        self.xoa_frame.grid_forget()

    def xoavtcv(self):
        self.sua_frame.grid_forget()
        self.them_frame.grid_forget()
        self.xem_frame.grid_forget()
        self.xoa_frame.grid(row=0, column=0, sticky="nsew")

    def maCV(self, event=None):
        DalPositionjob.create_connection()
        data = DalPositionjob.get_macv()
        self.comboboxmaCV_xoa['values'] = data  # Populate combobox for delete
        self.comboboxmaCV_sua['values'] = data  # Populate combobox for edit
        if data:
            self.comboboxmaCV_xoa.set(data[0])  # Set the first item as default
            self.comboboxmaCV_sua.set(data[0])  # Set the first item as default
            self.on_combobox_select()  # Call the function to update other fields

    def on_combobox_select(self, event=None):
        maCV = self.comboboxmaCV_xoa.get()
        DalPositionjob.create_connection()
        tencv = DalPositionjob.get_tencv(maCV)
        self.name_entry.delete(0, 'end')
        self.name_entry.insert(0, tencv[0][0])

    def on_combobox_select_sua(self, event=None):
        maCV = self.comboboxmaCV_sua.get()
        DalPositionjob.create_connection()
        tencv = DalPositionjob.get_tencv(maCV)
        self.name_entry1.delete(0, 'end')
        self.name_entry1.insert(0, tencv[0][0])
        self.hesoluong_entry1.delete(0, 'end')  # Xóa hết thông tin trước đó trong entry field
        self.hesoluong_entry1.insert(0, tencv[0][1])  # Chèn hệ số lương từ cơ sở dữ liệu vào entry field

    def suathongtin(self):
        tencv = self.name_entry1.get()
        hesoluong = self.hesoluong_entry1.get()

        if not (self.comboboxmaCV_sua.get() and tencv and hesoluong):
            messagebox.showinfo("Thông báo", "Không để trống")
            return
        else:
            DalPositionjob.create_connection()
            DalPositionjob.update_positionjob(self.comboboxmaCV_sua.get(), tencv, hesoluong)
            messagebox.showinfo("Thông báo", "Sửa vị trí công việc thành công")
            self.sua_frame.grid_forget()
            self.maCV()
            self.update_xem_frame_data()

    def save_department(self):
        tencv = self.tencv_entry.get()
        hesoluong = self.hesoluong_entry.get()
        macv = self.maCV()
        if not (tencv and hesoluong):
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        else:
            DalPositionjob.create_connection()
            DalPositionjob.insert_positionjob(macv,tencv, hesoluong)
            messagebox.showinfo("Thông báo", "Thêm vị trí công việc thành công")
            self.them_frame.grid_forget()
            self.update_xem_frame_data()

    def xoathongtin(self):
        result = messagebox.askokcancel("Xác nhận", "Xác nhận xóa?")
        if result:
            DalPositionjob.create_connection()
            temp = DalPositionjob.delete_positionjob(self.comboboxmaCV_xoa.get())
            if temp == -1:
                messagebox.askokcancel("Thông báo", "Không thể xóa phòng ban. Vẫn còn nhân viên làm việc ở phòng ban này.")
            self.xoa_frame.grid_forget()
            self.update_xem_frame_data()

    def update_xem_frame_data(self):
        self.tree.delete(*self.tree.get_children())  # Clear existing data

        columns = ('MaViTriCongViec', 'TenViTriCongViec', 'HeSoLuong')
        DalPositionjob.create_connection()
        data = DalPositionjob.get_all_positionjob()

        for row in data:
            self.tree.insert('', 'end', values=row)

if __name__ == "__main__":
    app = PositionManagementApp()
    app.mainloop()
