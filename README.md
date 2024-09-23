# 👻 Face Tracker: The Ghostbuster of Your Webcam!

Welcome to **Face Tracker**, the ultimate Django application that not only tracks your face in real-time but also sends you SMS alerts with photo-link (i used Firestore) when an unrecognized face photobombs your webcam! Whether it's a friend sneaking up on you or a ghost trying to make an appearance, this app has got your back (and your front), with alerts like: 

"A ghost just photobombed ::: time to kick an ectoplasmic butt > http://fa.ly/photo". 

Note: 

Make sure your camera’s IP address is static or use a dynamic DNS service to keep it accessible. If you’re accessing the camera from another city, ensure that your internet connection and firewall settings allow external access.

In case it is DDNS, the url, to access cam, would be somewhat liek this : ip_camera_url = "http://mycamera.ddns.net:8080/video"

## 🎉 Features
- **Real-time Face Detection**: Using OpenCV, this app can detect faces faster than you can say "cheese!"
- **Face Tracking**: Move left, right, or do a little dance, and watch as the app follows your every move.
- **Color-Coded Rectangles**: Green for known faces (friends), red for unknown faces (potential ghosts).
- **Web Interface**: Stream your video feed via a Django web interface. Perfect for showing off your dance moves!
- **SMS Alerts**: Get notified via SMS when an unrecognized face is detected. Because who doesn't want to know when a ghost is lurking?

## 🛠️ Prerequisites
Before you dive in, make sure you have the following installed:
- **Python 3.x**: The magic potion for running this app.
- **Django**: Install via `pip install django`
- **OpenCV**: Install via `pip install opencv-python`
- **Numpy**: Install via `pip install numpy`
- **Requests**: Install via `pip install requests`
- **Face Recognition**: Install via `pip install face_recognition`
- **python-dotenv**: Install via `pip install python-dotenv`

Optional for advanced face detection:
- **TensorFlow**: Install via `pip install tensorflow` (if you want to get fancy).

## 🚀 Installation and Setup

### 1. Clone the Repository

### 2. Install Dependencies

i haven't filled this file, i'm too lazy to fill this up

```bash
pip install -r requirements.txt

```

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
Open your web browser and navigate to `http://127.0.0.1:8000/`. For ip_camera_url = "http://49.115.190.152:8080/video" (change the IP that you have). You should see your webcam feed. Smile for the camera!

## 📸 Usage

1. **Adding Recognized Faces**: You can add recognized faces by placing images in the specified directory and using the `/add_face/` endpoint to upload them.
2. **Face Tracking**: The application will automatically track your face and send an SMS alert if an unrecognized face is detected. Perfect for keeping unwanted guests at bay!

Your `views.py` file currently focuses on adding recognized faces from Firestore and streaming the video feed. The handling of unknown faces and sending SMS alerts is primarily managed in your `camera.py` file, particularly in the `VideoCamera` class.

### Here’s how it works:

1. **Camera.py:**
   - In the `get_frame` method, unknown faces are detected, and their images are uploaded to Firestore.
   - The public URL of the uploaded image is sent via SMS using the `send_sms_alert` method.

2. **Views.py:**
   - You don’t need to add any code specifically for handling unknown faces here unless you want to create a separate view to display or manage those unknown face records.
   - If you want to implement features like viewing unknown faces in your web app or managing them, you can add new views and templates for that purpose.

## 🤝 Contributing
We welcome contributions to this project! If you have any suggestions, improvements, or just want to share a funny ghost story, please feel free to submit a pull request.

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## 🏗️ App Structure
```
├── face_tracker/
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── README.md
│   ├── .env
│   ├── manage.py
│   ├── config/
│   │   ├── firebase-adminsdk.json
│   │   └── firebase_config.py
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
│   │   ├── utils.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │   ├── templates/
│   │   │   └── index.html
```

## 🎭 Final Thoughts
With **Face Tracker**, you can keep an eye on your surroundings while having a bit of fun. Whether you're monitoring your home or just want to see who’s sneaking up on you, this app is your trusty sidekick. So, get ready to track those faces and send some ghostly SMS alerts!

Happy tracking! 👻
