# Face Tracking Django App using OpenCV

This Django application tracks your face in real-time using **OpenCV**. As you move, the app draws a rectangle around your face and follows it. It captures live video from your webcam and displays it on a webpage. Extend this by using TensorFlow’s Object Detection API for more advanced models if needed.

## Features
- Real-time face detection using OpenCV.
- Tracks your face as you move left, right, or walk.
- Rectangle is drawn around the detected face.
- Streams video feed via a Django web interface.

## Prerequisites

Make sure you have the following installed:
- **Python 3.x**
- **Django** (Install via `pip install django`)
- **OpenCV** (Install via `pip install opencv-python`)
- **Numpy** (Install via `pip install numpy`)

Optional for advanced face detection:
- **TensorFlow** (Install via `pip install tensorflow`)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sachnaror/face-tracking-django-app.git
cd face-tracking-django-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt (i havent updated this app)
```

### 3. Run the Django Development Server

```bash
python manage.py runserver
```

### 4. Access the Application

Open your web browser and navigate to `http://127.0.0.1:8000/`. You should see your webcam feed.

## Contributing

We welcome contributions to this project! If you have any suggestions or improvements, please feel free to submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


```
├── face_tracker/
│   ├── requirements.txt (i havent updated this app)
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

