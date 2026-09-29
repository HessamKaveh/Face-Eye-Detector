# Face & Eye Detector

A real-time face and eye detection system built with Python and OpenCV.

The project supports both webcam-based detection and image-based detection.

## Features

- Real-time face detection
- Eye detection inside detected faces
- Webcam support
- Image-based detection
- Face and eye counting
- FPS monitoring
- Detection result visualization
- Lightweight and CPU-friendly implementation

## Technologies

- Python
- OpenCV
- NumPy
- Haar Cascade Classifiers

## Project Structure

```text
face-eye-detector/
│
├── src/
│   ├── main.py
│   ├── detector.py
│   ├── image_detector.py
│   └── utils.py
│
├── images/
│   └── test.jpg
│
├── outputs/
│   └── result.jpg
│
├── requirements.txt
├── .gitignore
└── README.md

```

## Installation

Clone the repository:

git clone https://github.com/HessamKaveh/face-eye-detector.git
cd face-eye-detector

## Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

## Install dependencies:

pip install -r requirements.txt

## Webcam Detection

Run:

python src/main.py


The application opens the webcam and displays:

Number of detected faces
Number of detected eyes
Current FPS

Press q or ESC to exit.

## Image Detection

# Place an image at:

images/test.jpg

# Then run:

python src/image_detector.py


# The processed image will be saved to:

outputs/result.jpg

## Detection Method

## The project uses OpenCV Haar Cascade classifiers.

## The face detector uses:

haarcascade_frontalface_default.xml

## The eye detector uses:

haarcascade_eye.xml


The eye detector is applied only inside detected face regions.

## Limitations

Haar Cascade detection can be affected by:

- Poor lighting
- Large head rotations
- Occlusion
- Very small faces
- Extreme facial angles





## Author
Hessam Kaveh — Research Fellow, Italian Institute of Technology
