from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import cv2
import sys


def face():
    """
    人脸识别
    """
    cap = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while (True):
        # 循环捕获每一帧
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        print("发现{0} 人脸!".format(len(faces)))
        if len(faces) != 0:
            return True
        else:
            return False
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按键q停止显示
            break


# 关闭
    # cap.release()
    # cv2.destroyAllWindows()

# face()


# subject = ["", "Ramiz Raja", "cat king"]

# def detect_face(img):
#     gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
#     faca_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
#     faces = faca_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

#     if (len(face) == 0):
#         return None, None
        
#     (x, y, w, h) = faces[0]
#     return gray[y:y + w, x:x + h], faces[0]

#     image = cv2.imread("training-data/s1/1.jpg")
#     face, rect = detect_face(image)
#     print(rect)
#     cv2.imshow("hello", cv2.resize(face, (400,500)))
#     cv2.waitKey()
#     cv2.destroyAllWindows()


# def prepare_training_data(data_folder_path):
#     dirs = os.listdir(data_folder_path)
#     faces = []
#     labels = []
#     for dir_name in dirs:
#         if not dir_name.startswith("s"):
#             continue;
#         label = int(dir_name.replace("s", ""))
        
#         subject_dir_path = data_folder_path + "/" + dir_name
#         subject_images_names = os.listdir(subject_dir_path)
#         for image_name in subject_images_names:
#             if image_name.startswith("."):
#                 continue;
#             image_path = subject_dir_path + "/" + image_name
#             image = cv2.imread(image_path)
#             cv2.imshow("Training on image...", cv2.resize(image,(400, 500)))
#             cv2.waitKey(100)
#             face, rect = detect_face(image)
#             if face is not None:
#                 faces.append(face)
#                 labels.append(label)
#         cv2.destroyAllWindows()
#         cv2.waitKey(1)
#         cv2.destroyAllWindows()
#         return faces, labels

#         faces, labels = prepare_training_data("training-data")
#         print("Data prepared")
#         print("Total faces:", len(faces))
#         print("Total labels:", len(labels))


#         # 使用LBPH人脸识别器：
#         # 创建LBPH人脸识别器
#         face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#         # 训练面部识别器
#         face_recognizer.train(faces, np.array(labels))
#         # 在图像上绘制矩形,根据给定的（x，y）坐标和给定的宽度和高度 （预测）
#         def draw_rectangle(img, rect):
#             (x, y, w, h) = rect
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         # 从图像开始绘制文本,通过（x，y）坐标。
#         def draw_text(img, text, x, y):
#             cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


# def predict(test_img):
#     img = test_img.copy()  # 制作图像的副本，不想更改原始图像
#     face, rect = detect_face(img) # 从图像中检测脸部
#     label, confidence = face_recognizer.predict(face)# 使用脸部识别器预测图像
#     label_text = subjects[label] # 获取由人脸识别器返回的相应标签的名称
#     # 在检测到的脸部周围画一个矩形
#     draw_rectangle(img, rect)
#     # 画出预计人的名字
#     draw_text(img, label_text, rect[0], rect[1] - 5)
#     return img

#     print("Predicting images...")
#     #加载测试图像
#     test_img1 = cv2.imread("test-data/test1.jpg")
#     test_img2 = cv2.imread("test-data/test2.jpg")
#     #执行预测
#     predicted_img1 = predict(test_img1)
#     predicted_img2 = predict(test_img2)
#     print("Prediction complete")
#     #显示两个图像
#     cv2.imshow(subjects[1], predicted_img1)
#     cv2.imshow(subjects[2], predicted_img2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# 临时人脸识别存在有道云笔记 python开发 下