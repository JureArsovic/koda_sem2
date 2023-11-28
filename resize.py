from PIL import Image
import os

def resize_image(input_path, output_path, size=(1000, 1500)):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.Resampling.LANCZOS)
        img.save(output_path)

def process_images(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(directory, filename)
            with Image.open(file_path) as img:
                if img.size != (1000, 1500):
                    print(f"Resizing image: {filename}")
                    resize_image(file_path, file_path)
                else:
                    print(f"Image already correct size: {filename}")

# Run the script in the current directory
process_images('./posters')
