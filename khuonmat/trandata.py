
import numpy as np
import os
from PIL import Image
import DALanh

def training():
    def model(dict):
        TRAIN_DATA = 'khuonmat/dataface'
        TEST_DATA = 'khuonmat/datafacetest'
        Xtrain = []
        Ytrain = []
        Xtest = []
        Ytest = []

        # dict = {'1trinh': [0, 0, 0, 0, 1], '2nguyen': [0, 0, 0, 1, 0], '3vy': [0, 0, 0, 1, 1]}

        def getData(dirData, listData):
            for whatever in os.listdir(dirData):
                whatever_path = os.path.join(dirData, whatever)
                list_filename_path = []
                for filename in os.listdir(whatever_path):
                    filename_path = os.path.join(whatever_path, filename)
                    label = filename_path.split('\\')[1]
                    img = np.array(Image.open(filename_path))
                    list_filename_path.append((img, dict[label]))
                listData.extend(list_filename_path)
            return listData
        # đoạn code này đọc tất cả các hình ảnh trong các thư mục con của dirData, 
        # tạo ra các cặp (hình ảnh/ nhãn)và lưu trữ chúng trong danh sách listData.
        Xtrain = getData(TRAIN_DATA, Xtrain)
        #đọc ảnh từ foder
        Xtest = getData(TEST_DATA, Xtest)

        np.random.shuffle(Xtrain)
        np.random.shuffle(Xtest)
        #  trộn dữ liệu để tăng khả năng tranining

        import tensorflow as tf
        from tensorflow.keras import layers, models
        # mô hình Mạng Nơ-ron Tích chập (Convolutional Neural Network - CNN) bằng thư viện Keras
        model_training_first = models.Sequential([
            layers.Conv2D(32, (3, 3), input_shape=(180, 180, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.15),

            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.2),

            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Dropout(0.2),

            layers.Flatten(),
            layers.Dense(100, activation='relu'),
            layers.Dense(256, activation='relu'),
            layers.Dense(5, activation='softmax')
        ])

        model_training_first.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model_training_first.fit(np.array([x[0] for x in Xtrain]), np.array([x[1] for x in Xtrain]), epochs=10)
        if os.path.exists('khuonmat/modelfacefinal2.h5'):
        # Xóa tệp tin nếu tồn tại
            os.remove('modelfacefinal2.h5')
            print(f"Đã xóa tệp ")
        else:
            print(f"Tệp  không tồn tại")
        model_training_first.save('khuonmet/modelfacefinal2.h5')
    def xulydauvao(input_data_array):
        result = []

        for input_data in input_data_array:
            # Tách tên và số từ dữ liệu đầu vào
            name, number = input_data.split('-')
            number = int(number)

            # Chuyển đổi số thành chuỗi nhị phân và tạo danh sách số nhị phân
            binary_string = bin(number)[2:].zfill(5)
            if len(binary_string) > 5:
                binary_string = binary_string[-5:]

            binary_list = [int(bit) for bit in binary_string]

            # Gán tên và giá trị vào từ điển
            data = {name: binary_list}

            result.append(data)

        return result
    DALanh.create_connection()
    input_array = DALanh.get_all_records()
    result = xulydauvao(input_array)
    new_dict = {}
    for item in result:
        key = list(item.keys())[0]
        value = item[key]
        new_dict[key] = value
    model(new_dict)