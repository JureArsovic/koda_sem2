import tkinter as tk
from tkinter import Label, Button, filedialog
from PIL import Image, ImageTk
from styling import setup_styles
from logic import upload_image, capture_image_from_webcam, primerjaj

# Function to handle button clicks
def handle_upload_and_primerjaj():
    upload_image(root, image_label, style)
    result = sorted(primerjaj('barve.txt', './img/upload.png'))
    najblizja = result[0][2] if result else "No result"
    status_label.config(text=f"Status: Result - {najblizja}")
    display_poster(result)

def handle_capture_and_primerjaj():
    capture_image_from_webcam(root, image_label, style)
    result = sorted(primerjaj('barve.txt', './capturedImages/CapturedImage.png'))
    najblizja = result[0][2] if result else "No result"
    status_label.config(text=f"Status: Result - {najblizja}")
    display_poster(result)

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
        poster_path = f"./posters/{result[0][2]}"
        poster_image = Image.open(poster_path)
        poster_image = poster_image.resize((300, 300), Image.Resampling.LANCZOS)
        poster_photo = ImageTk.PhotoImage(poster_image)
        poster_label.config(image=poster_photo)
        poster_label.image = poster_photo
        poster_label.configure(text="Poster", compound="top")
    else:
        poster_label.configure(image='', text="No result")

root.mainloop()
