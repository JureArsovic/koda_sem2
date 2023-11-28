import tkinter as tk
from tkinter import Label, Button
from styling import setup_styles
from logic import upload_image, capture_image_from_webcam

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

upload_button = Button(content, text="Upload Image", command=lambda: upload_image(root, image_label, style), **style["button"])
upload_button.pack(pady=20)

capture_button = Button(content, text="Capture Image", command=lambda: capture_image_from_webcam(root, image_label, style), **style["button"])
capture_button.pack(pady=20)

# Footer
status_label = Label(footer, text="Status: Ready", **style["label"])
status_label.pack(side="left", padx=20)

root.mainloop()
