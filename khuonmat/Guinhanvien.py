import tkinter as tk

class FunctionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Function App")
        self.geometry("500x500")

        # Tạo khung chính
        self.main_frame = tk.Frame(self, width=500, height=500)
        self.main_frame.pack(fill="both", expand=True)

        # Tạo 4 cột đầu
        self.function_frame = tk.Frame(self.main_frame, width=100, height=500)
        self.function_frame.pack(side="left", fill="y")

        self.view_btn = tk.Button(self.function_frame, text="View", command=self.show_view)
        self.view_btn.pack(pady=10)

        self.add_btn = tk.Button(self.function_frame, text="Add", command=self.show_add)
        self.add_btn.pack(pady=10)

        self.edit_btn = tk.Button(self.function_frame, text="Edit", command=self.show_edit)
        self.edit_btn.pack(pady=10)

        self.delete_btn = tk.Button(self.function_frame, text="Delete", command=self.show_delete)
        self.delete_btn.pack(pady=10)

        # Tạo giao diện chính
        self.content_frame = tk.Frame(self.main_frame, width=400, height=500)
        self.content_frame.pack(side="left", fill="both", expand=True)

        # Tạo giao diện cho phần "Add"
        self.add_frame = tk.Frame(self.content_frame, width=400, height=500)
        self.name_label = tk.Label(self.add_frame, text="Name:")
        self.name_entry = tk.Entry(self.add_frame)
        self.save_btn = tk.Button(self.add_frame, text="Save", command=self.save_item)

        # Tạo giao diện cho phần "View"
        self.view_frame = tk.Frame(self.content_frame, width=400, height=500)
        self.view_label = tk.Label(self.view_frame, text="This is the View function")

        # Tạo giao diện cho phần "Edit"
        self.edit_frame = tk.Frame(self.content_frame, width=400, height=500)
        self.edit_label = tk.Label(self.edit_frame, text="This is the Edit function")
        self.edit_entry = tk.Entry(self.edit_frame)
        self.save_edit_btn = tk.Button(self.edit_frame, text="Save", command=self.save_edit)

        # Tạo giao diện cho phần "Delete"
        self.delete_frame = tk.Frame(self.content_frame, width=400, height=500)
        self.delete_label = tk.Label(self.delete_frame, text="This is the Delete function")
        self.delete_btn = tk.Button(self.delete_frame, text="Delete", command=self.delete_item)

    def show_view(self):
        self.hide_all_frames()
        self.view_frame.pack(side="left", fill="both", expand=True)
        self.view_label.pack(pady=20)

    def show_add(self):
        self.hide_all_frames()
        self.add_frame.pack(side="left", fill="both", expand=True)
        self.name_label.pack(pady=10)
        self.name_entry.pack(pady=10)
        self.save_btn.pack(pady=10)

    def show_edit(self):
        self.hide_all_frames()
        self.edit_frame.pack(side="left", fill="both", expand=True)
        self.edit_label.pack(pady=20)
        self.edit_entry.pack(pady=10)
        self.save_edit_btn.pack(pady=10)

    def show_delete(self):
        self.hide_all_frames()
        self.delete_frame.pack(side="left", fill="both", expand=True)
        self.delete_label.pack(pady=20)
        self.delete_btn.pack(pady=10)

    def hide_all_frames(self):
        for frame in [self.add_frame, self.view_frame, self.edit_frame, self.delete_frame]:
            frame.forget()

    def save_item(self):
        # Lưu dữ liệu mới
        pass

    def save_edit(self):
        # Lưu dữ liệu chỉnh sửa
        pass

    def delete_item(self):
        # Xóa dữ liệu
        pass

if __name__ == "__main__":
    app = FunctionApp()
    app.mainloop()