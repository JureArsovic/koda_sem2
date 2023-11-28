import tkinter as tk
import os
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from cv2 import VideoCapture, destroyAllWindows, imshow, imwrite, waitKey


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
        except Exception as e:
            print(f"Error opening image: {e}")


def capture_image_from_webcam(root, image_label, style):
    cam_port = 0
    cam = VideoCapture(cam_port)

    if not cam.isOpened():
        messagebox.showerror("Error", "Camera could not be opened.")
        return

    while True:
        result, frame = cam.read()

        if not result:
            messagebox.showerror("Error", "Failed to capture image from camera.")
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
            image = image.resize((base_width, h_size), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            image_label.config(image=photo)
            image_label.image = photo  # Keep a reference!
            break

    cam.release()
    destroyAllWindows()
