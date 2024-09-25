
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import DALanh
def testface(name):
    # Load the pre-trained model
    DALanh.create_connection()
    input_array = DALanh.get_all_names()
    listall =input_array
    face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    model = load_model('pydoan/khuonmat/modelfacefinal.h5')

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        OK, frame = cap.read()
        if not OK:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            roi = cv2.resize(frame[y+2:y+h-2, x+2:x+w-2], (180, 180))
            result = np.argmax(model.predict(roi.reshape((-1, 180, 180, 3))))
            cv2.rectangle(frame, (x, y), (x+w, y+h), (180, 244, 50), 1)
            cv2.putText(frame, listall[result], (x+15, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 25, 255), 2)
            if(name==listall[result]):
                return 1
        cv2.imshow('FRAME', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
