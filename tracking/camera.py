# tracking/camera.py
import cv2


class VideoCamera:
    def __init__(self):
        # Open webcam
        self.video = cv2.VideoCapture(0)
        # Load pre-trained face detection model (Haar Cascade)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        # Convert to grayscale for faster face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Draw rectangle around the detected face(s)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Encode the frame to send it as a stream to the webpage
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
