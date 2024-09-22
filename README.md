# App-on-Camera tracks faces live; SMS you for an unrecognized face photo link.

This python app-on-camera tracks your face in real-time. Sends SMS alerts for unrecognized faces. 
Red Tracker=UnKnown face, Green=known face.  

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

### 2. Install Dependencies

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add your Twilio API credentials:

```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_number
RECEIVER_PHONE_NUMBER=your_receiver_number
DEBUG=True
```

### 4. Run the Django Development Server

```bash
python manage.py runserver
```

### 5. Access the Application

Open your web browser and navigate to `http://127.0.0.1:8000/`. You should see your webcam feed.

## Usage

1. **Adding Recognized Faces**: You can add recognized faces by placing images in the specified directory and using the `/add_face/` endpoint to upload them.
2. **Face Tracking**: The application will automatically track your face and send an SMS alert if an unrecognized face is detected.

## Contributing

We welcome contributions to this project! If you have any suggestions or improvements, please feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## App Structure

```

├── face_tracker/
│   ├── requirements.txt (i left it empty)
│   ├── db.sqlite3
│   ├── README.md
│   ├── .env
│   ├── manage.py
│   ├── face_tracker/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── tracking/
│   │   ├── models.py
│   │   ├── apps.py
│   │   ├── camera.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │   ├── templates/
│   │   │   └── index.html
