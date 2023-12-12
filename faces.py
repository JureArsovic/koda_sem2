import cv2
import os

def save_largest_face_from_directory():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Directory containing images
    posters_dir = 'posters'
    faces_dir = 'faces'

    # Create faces directory if it doesn't exist
    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)

    # Process each file in the posters directory
    for filename in os.listdir(posters_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for image files
            img_path = os.path.join(posters_dir, filename)
            img = cv2.imread(img_path)

            # Check if image is loaded
            if img is None:
                print(f"Error: Image {filename} not found.")
                continue

            # Convert into grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            if len(faces) == 0:
                print(f"No faces found in {filename}")
                continue

            # Find the largest face
            largest_face = max(faces, key=lambda face: face[2] * face[3])

            # Extract the largest face
            x, y, w, h = largest_face
            face = img[y:y+h, x:x+w]

            # Save the face
            cv2.imwrite(os.path.join(faces_dir, filename), face)

save_largest_face_from_directory()
