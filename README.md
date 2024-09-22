# Face Tracking Django App using OpenCV

This Django application tracks your face in real-time using **OpenCV**. As you move, the app draws a rectangle around your face and follows it. It captures live video from your webcam and displays it on a webpage. The application also sends SMS alerts for unrecognized face detection using Twilio's API.

## Features
- Real-time face detection using OpenCV.
- Tracks your face as you move left, right, or walk.
- Rectangle is drawn around the detected face.
- Streams video feed via a Django web interface.
- Sends SMS alerts for unrecognized faces.

## Prerequisites

Make sure you have the following installed:
- **Python 3.x**
- **Django** (Install via `pip install django`)
- **OpenCV** (Install via `pip install opencv-python`)
- **Numpy** (Install via `pip install numpy`)
- **Requests** (Install via `pip install requests`)
- **Face Recognition** (Install via `pip install face_recognition`)
- **python-dotenv** (Install via `pip install python-dotenv`)

Optional for advanced face detection:
- **TensorFlow** (Install via `pip install tensorflow`)

## Installation and Setup

### 1. Clone the Repository
