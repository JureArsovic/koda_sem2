import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from cv2 import VideoCapture, destroyAllWindows, imshow, imwrite, waitKey
import numpy as np
import re
import ast
import extcolors
import cv2
from deepface import DeepFace


def upload_image(root, image_label, style):
    file_types = [('JPEG Files', '*.jpeg;*.jpg'), ('PNG Files', '*.png')]
    file_path = filedialog.askopenfilename(filetypes=file_types)

    if file_path:
        try:
            original_image = Image.open(file_path)

            display_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(display_image)

            if image_label:
                image_label.config(image=photo)
                image_label.image = photo
            else:
                image_label = tk.Label(root, image=photo, bg=style["bg"])
                image_label.image = photo
                image_label.pack()

            img_dir = os.path.join(os.getcwd(), "img")
            os.makedirs(img_dir, exist_ok=True)
            img_save_path = os.path.join(img_dir, "upload.png")
            original_image.save(img_save_path)

        except Exception as e:
            print(f"Error opening image: {e}")



def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Detected Faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def capture_image_from_webcam(root, image_label, style):
    cam_port = 0
    cam = VideoCapture(cam_port)

    if not cam.isOpened():
        messagebox.showerror("Error", "Camera could not be opened.")
        return

    while True:
        result, frame = cam.read()

        if not result:
            messagebox.showerror(
                "Error", "Failed to capture image from camera.")
            break

        imshow("Camera - Press 'c' to capture", frame)

        if waitKey(1) == ord('c'):
            image_path = "capturedImages/CapturedImage.png"
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            imwrite(image_path, frame)
            messagebox.showinfo("Success", "Image captured and saved.")

            image = Image.open(image_path)
            base_width = 300
            w_percent = (base_width / float(image.size[0]))
            h_size = int((float(image.size[1]) * float(w_percent)))

            image = image.resize((base_width, h_size),
                                 Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            image_label.config(image=photo)
            image_label.image = photo  # Keep a reference!
            break

    cam.release()
    destroyAllWindows()


def ujemanjeFun(poster, slika):
    dist = [0, 0, 0, 0]
    ujemanje = 0

    for i in range(len(poster)):
        sestevekDolzin = 0
        for j in range(len(poster[i][0])):
            sestevekDolzin += abs(poster[i][0][j]-slika[0][i][0][j])
            # print(poster[i][0][j])
            # print(slika[0][i][0][j])
        dist[i] = sestevekDolzin

    dist[0] = dist[0]*0.6
    dist[1] = dist[1]*0.3
    dist[2] = dist[2]*0.1
    dist[3] = dist[3]*0.05

    # print(dist)
    ujemanje = dist[0] + dist[1] + dist[2] + dist[3]
    # print(ujemanje)
    return ujemanje


def primerjaj(dataFile_path, pictureFile_path):
    with open(dataFile_path, 'r') as file:
        data = file.read()

    colors = extcolors.extract_from_path(pictureFile_path)
    del colors[0][4:]

    dataTransformed = ast.literal_eval(data)
    # print(dataTransformed[1][1])

    seznamPosterjev = []

    for i in range(len(dataTransformed)):
        dataTransformed[i][1] = dataTransformed[i][1][:4]
        # print("DATATRANSFORMED Z INDEKSOM ", i, "  --   ",dataTransformed[i][1])
        # print("COLORS OF SELECTED IMAGE: ", colors[0])
        seznamPosterjev.append(
            (ujemanjeFun(dataTransformed[i][1], colors), i, dataTransformed[i][0]))

    return seznamPosterjev

def save_largest_face():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    img_path = 'capturedImages/CapturedImage.png'
    face_dir = 'capturedImages/face'

    if not os.path.exists(face_dir):
        os.makedirs(face_dir)

    img = cv2.imread(img_path)

    if img is None:
        print(f"Error: Image {img_path} not found.")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        print(f"No faces found in {img_path}")
        return

    # Find the largest face
    largest_face = max(faces, key=lambda face: face[2] * face[3])
    x, y, w, h = largest_face
    face = img[y:y+h, x:x+w]

    cv2.imwrite(os.path.join(face_dir, 'CapturedImage.png'), face)

def save_largest_face_upload():
    #cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img_path = 'img/upload.png'
    face_dir = 'img/face'

    if not os.path.exists(face_dir):
        os.makedirs(face_dir)

    img = cv2.imread(img_path)

    if img is None:
        print(f"Error: Image {img_path} not found.")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        print(f"No faces found in {img_path}")
        return

    # Find the largest face
    largest_face = max(faces, key=lambda face: face[2] * face[3])
    x, y, w, h = largest_face
    face = img[y:y+h, x:x+w]

    cv2.imwrite(os.path.join(face_dir, 'upload.png'), face)

def imageSimilarity(img1, img2):
    #print("Image similarity: ", img1, img2)
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)
    hist_img1 = cv2.calcHist([image1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    hist_img1[255, 255, 255] = 0
    cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_img2 = cv2.calcHist([image2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    hist_img2[255, 255, 255] = 0
    cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
    #print(f"Similarity Score: ", round(metric_val, 2))
    return metric_val

def combine(arr1, arr2):
    arr1 = scale_tuple_values(arr1)
    arr2 = scale_tuple_values(arr2)
    #print(sorted(arr1))
    #print(sorted(arr2))
    combined = []

    # Iterate through both arrays
    for (a, _), (c, _, g) in zip(arr1, arr2):
        f = 0.6 * a + 0.4 * (1-c)
        combined.append((f, g))
    combined.sort(reverse=True)
    print(combined)

    return combined
    




def scale_tuple_values(arr):
    # Extract first values from each tuple in the array
    values = [item[0] for item in arr]

    # Min-max scaling for these values
    min_val, max_val = min(values), max(values)
    scaled_values = [(val - min_val) / (max_val - min_val) if max_val > min_val else 0 for val in values]

    # Create a new array with scaled values while keeping the other elements of the tuples intact
    scaled_arr = [(scaled_values[idx],) + arr[idx][1:] for idx in range(len(arr))]

    return scaled_arr

primerjaj('barve.txt', './img/upload.png')