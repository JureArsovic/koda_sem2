import json
import os
import tkinter as tk
from tkinter import Label, Button, filedialog
from PIL import Image, ImageTk
import numpy as np
from styling import setup_styles
import face_recognition
from logic import upload_image, capture_image_from_webcam, primerjaj, save_largest_face, save_largest_face_upload, imageSimilarity, combine

#FACE DETECTION -> OPENCV (+ TRAINED CLASSIFIER XML FILE)
#FACE comparison -> HISTOGRAM COMPARISON (NON WHITE PIXELS)

def handle_upload_and_primerjaj():
    upload_image(root, image_label, style)
    save_largest_face_upload()
    similarity_results = []
    faces_dir = 'faces'
    img1 = './img/face/upload.png'
    image1 = face_recognition.load_image_file(img1)
    face_encodings_1 = face_recognition.face_encodings(image1)
    with open('fVectors.txt', 'r') as file:
        feature_vectors = json.load(file)
    i = 0
    for filename in os.listdir(faces_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            feature_vector_index = np.array(feature_vectors[i])
            similarity_index = imageSimilarity(face_encodings_1, feature_vector_index)
            i = i + 1
            similarity_results.append((similarity_index, filename))
    i = 0
    result = primerjaj('barve.txt', './img/upload.png')
    combined = combine(similarity_results, result)
    najblizja = combined[0][1] if result else "No result"
    status_label.config(text=f"Status: Result - {najblizja}")
    display_poster(najblizja)


def handle_capture_and_primerjaj():
    capture_image_from_webcam(root, image_label, style)
    save_largest_face()
    similarity_results = []
    faces_dir = 'faces'
    img1 = './capturedImages/face/CapturedImage.png'
    image1 = face_recognition.load_image_file(img1)
    face_encodings_1 = face_recognition.face_encodings(image1)
    with open('fVectors.txt', 'r') as file:
        feature_vectors = json.load(file)
    i = 0
    for filename in os.listdir(faces_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            feature_vector_index = np.array(feature_vectors[i])
            similarity_index = imageSimilarity(face_encodings_1, feature_vector_index)
            i = i + 1
            similarity_results.append((similarity_index, filename))
    i = 0
    result = primerjaj('barve.txt', './capturedImages/CapturedImage.png')
    combined = combine(similarity_results, result)
    najblizja = combined[0][1] if result else "No result"
    status_label.config(text=f"Status: Result - {najblizja}")
    display_poster(najblizja)


root = tk.Tk()
root.title("Image Upload Example")
root.state('zoomed')

style = setup_styles()

# Layout
header = tk.Frame(root, bg=style["bg"], height=50)
content = tk.Frame(root, bg=style["bg"])
footer = tk.Frame(root, bg=style["bg"], height=30)
header.pack(fill='x')
content.pack(fill='both', expand=True)
footer.pack(fill='x')

# Header
app_title = Label(header, text="Image Uploader", **style["label"], font=("Arial", 16, "bold"))
app_title.pack(side="left", padx=20)

# Content
image_label = tk.Label(content, bg=style["bg"])
image_label.grid(row=0, column=0, padx=20, pady=20)

poster_label = tk.Label(content, bg=style["bg"])
poster_label.grid(row=0, column=1, padx=20, pady=20)

upload_button = Button(content, text="Upload Image", command=handle_upload_and_primerjaj, **style["button"])
upload_button.grid(row=1, column=0, padx=20, pady=20)

capture_button = Button(content, text="Capture Image", command=handle_capture_and_primerjaj, **style["button"])
capture_button.grid(row=1, column=1, padx=20, pady=20)

# Footer
status_label = Label(footer, text="Status: Ready", **style["label"])
status_label.pack(side="left", padx=20)


def display_poster(result):
    if result:
        poster_path = f"./posters/{result}"
        poster_image = Image.open(poster_path)
        poster_image = poster_image.resize((300, 300), Image.Resampling.LANCZOS)
        poster_photo = ImageTk.PhotoImage(poster_image)
        poster_label.config(image=poster_photo)
        poster_label.image = poster_photo
        poster_label.configure(compound="top")
    else:
        poster_label.configure(image='', text="No result")


root.mainloop()
