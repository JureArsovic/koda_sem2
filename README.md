# Face2Poster – AI Movie Poster Face Swapper

**Authors:** Erik Mažgon, Jure Arsovič  

## Overview  
Face2Poster is a computer vision and AI project that captures a user’s face through the webcam, compares it with all movie poster faces in the database, and seamlessly edits the user’s face into the selected movie poster. The result is a personalized, AI-generated movie poster starring you.  

This project combines face detection, recognition, and face-swapping models with traditional image processing, making it both a fun demo and a showcase of applied machine learning in multimedia.

---

## Features
- Real-time face capture from the webcam.  
- Face comparison against all faces stored in the movie posters database.  
- AI-powered face swapping into posters for realistic integration.  
- Poster editing and blending with colors and lighting adjustments.  

---

## Technologies & Libraries
- **Programming Language:** Python  
- **Computer Vision:** OpenCV, Face Recognition  
- **Deep Learning:** InsightFace (ONNX model `inswapper_128.onnx`)  
- **Image Processing:** Pillow, NumPy, SciPy, ExtColors  
- **Model Runtime:** ONNX Runtime  

---

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/face2poster.git
cd face2poster
```

### 2. Install Dependencies
```bash
pip install pillow numpy face-recognition opencv-python extcolors insightface scipy
```
### 3. Download Pretrained Model

Download the inswapper_128.onnx model from [Google Drive](https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view)

Place it into the project’s root folder.

### 4. Run the Application
```
python main.py
```
### 5. Have fun :)

## Example Workflow

1. The application captures your face through the webcam.

2. Your face is compared with all poster faces stored in the database.

3. A best-match poster is selected based on multiple criteira.

4. The system uses AI to swap your face into the poster.

5. A customized movie poster featuring you is generated.
