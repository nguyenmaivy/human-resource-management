import os
import cv2

def save_captured_image(folder_name):
    # Tạo thư mục nếu nó chưa tồn tại
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Khởi tạo webcam
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    # Load bộ phân loại khuôn mặt đã được huấn luyện trước
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Nhập ID khuôn mặt từ người dùng
    face_id = 1

    print('Đang thu thập ảnh khuôn mặt...')
    count = 0
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            cv2.imwrite(os.path.join(folder_name, f"User.{face_id}.{count}.jpg"), img[y:y + h, x:x + w])
            cv2.imshow('Ảnh', img)

        k = cv2.waitKey(100) & 0xFF
        if k == 27:  # Nhấn 'ESC' để thoát
            break
        elif count >= 50:  # Lấy 50 ảnh khuôn mặt và dừng
            break

    print("\nHoàn thành thu thập ảnh khuôn mặt.")
    cam.release()
    cv2.destroyAllWindows()

# Nhập tên thư mục và lưu ảnh vào dataface
def takephoto(name):
    folder_name = name

    data_dir = 'pydoan/khuonmat/dataface/' + folder_name
    save_captured_image(data_dir)

    # Lưu ảnh vào testdata
    test_data_dir = 'pydoan/khuonmat/datafacetest/' + folder_name
    save_captured_image(test_data_dir)
