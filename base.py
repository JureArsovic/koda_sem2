import cv2
from turtle import distance
import face_recognition
import face_recognition

image = face_recognition.load_image_file("./img/face/upload.png")
image2 = face_recognition.load_image_file("faces/Big Fat Quiz (2004).jpeg")
face_landmarks_list = face_recognition.face_landmarks(image)
face_encodings_1 = face_recognition.face_encodings(image)
face_encodings_2 = face_recognition.face_encodings(image2)
#smaller distance = more similar
distance = face_recognition.face_distance([face_encodings_1[0]], face_encodings_2[0])
#print(distance)
distance = distance[0]
print(distance)

""" face_encodings_1 = face_recognition.face_encodings(img1)
    face_encodings_2 = face_recognition.face_encodings(img2)
    distance = face_recognition.face_distance([face_encodings_1[0]], face_encodings_2[0])
    print(distance)
    distance = distance[0]
    print(distance) """