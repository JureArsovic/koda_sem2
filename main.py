import tkinter as tk
from tkinter import Label, Button
from styling import setup_styles
from logic import upload_image, capture_image_from_webcam, primerjaj

# Main application setup
root = tk.Tk()
root.title("Image Upload Example")
root.state('zoomed')

style = setup_styles()

# Layout using frames
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
image_label.pack(pady=20)


def handle_upload_and_primerjaj():
    upload_image(root, image_label, style)
    result = sorted(primerjaj('barve.txt', './img/upload.png'))
    najblizja = result[0][2] if result else "No result"
    print(result)
    status_label.config(text=f"Status: Result - {najblizja}")


def handle_capture_and_primerjaj():
    capture_image_from_webcam(root, image_label, style)  # Modify capture_image_from_webcam to return the file path
    result = sorted(primerjaj('barve.txt', './capturedImages/CapturedImage.png'))
    najblizja = result[0][2] if result else "No result"
    status_label.config(text=f"Status: Result - {najblizja}")


upload_button = Button(content, text="Upload Image", command=handle_upload_and_primerjaj, **style["button"])
upload_button.pack(pady=20)

capture_button = Button(content, text="Capture Image", command=handle_capture_and_primerjaj, **style["button"])
capture_button.pack(pady=20)

# Footer
status_label = Label(footer, text="Status: Ready", **style["label"])
status_label.pack(side="left", padx=20)

root.mainloop()
