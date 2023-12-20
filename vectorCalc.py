import face_recognition
import os
import json

# Path to the directory containing face images
directory = "./faces"

# Initialize an array to store feature vectors
feature_vectors = []

# Define a zero vector (128 zeros for face_recognition's feature vector)
zero_vector = [0] * 128

# Iterate over files in the directory
for filename in os.listdir(directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Check for valid file extensions
        file_path = os.path.join(directory, filename)

        # Load the image and extract feature vectors
        image = face_recognition.load_image_file(file_path)
        face_encodings = face_recognition.face_encodings(image)

        if face_encodings:
            # Assuming each image contains one face for simplicity
            feature_vectors.append(face_encodings[0])
        else:
            # Append a zero vector if no face is found
            feature_vectors.append(zero_vector)
            print(f"No faces found in {filename}, adding zero vector.")

# Save the feature vectors to a file
with open('fVectors.txt', 'w') as file:
    # Convert the list of numpy arrays to a list of lists for serialization
    feature_vectors_serializable = [list(vector) for vector in feature_vectors]
    json.dump(feature_vectors_serializable, file)

print("Feature vectors saved to fVectors.txt")
