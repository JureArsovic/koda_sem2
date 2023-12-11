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
            image = Image.open(file_path)
            image = image.resize((300, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            if image_label:
                image_label.config(image=photo)
                image_label.image = photo
            else:
                image_label = tk.Label(root, image=photo, bg=style["bg"])
                image_label.image = photo
                image_label.pack()

            # Save the image to the "/img" folder as "upload.png"
            img_dir = os.path.join(os.getcwd(), "img")
            os.makedirs(img_dir, exist_ok=True)
            img_save_path = os.path.join(img_dir, "upload.png")
            image.save(img_save_path)

        except Exception as e:
            print(f"Error opening image: {e}")


def detect_faces(image_path):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Read the input image
    img = cv2.imread(image_path)

    # Check if image is loaded
    if img is None:
        print("Error: Image not found.")
        return

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
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

            # Load the image
            image = Image.open(image_path)

            # Calculate new dimensions
            base_width = 300
            w_percent = (base_width / float(image.size[0]))
            h_size = int((float(image.size[1]) * float(w_percent)))

            # Resize the image maintaining the aspect ratio
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
    # Read the content of the data file
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
