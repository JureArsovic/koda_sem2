import extcolors
import os
from PIL import Image

def process_image(image_path):
    # Your image processing code goes here
    # For example, let's just write the image path to a new file for demonstration purposes
    result = f"Processed image: {image_path}\n"
    colors, pixel_count = extcolors.extract_from_path(image_path)

    #print(colors)
    # Write the result to a new file
    with open('barve.txt', 'a') as result_file:
        result_file.write(result + '\n' + str(colors) + '\n'+ '\n')

def process_images_in_folder(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Filter out non-image files (adjust the list of valid extensions as needed)
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = [file for file in files if any(file.lower().endswith(ext) for ext in valid_extensions)]

    # Process each image
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        process_image(image_path)

# Replace 'your_folder_path' with the path to your folder containing images
folder_path = './posters'
process_images_in_folder(folder_path)
