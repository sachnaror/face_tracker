# tracking/camera.py
import pickle

import cv2
import face_recognition
import numpy as np

from .models import RecognizedFace


class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.known_face_encodings = []  # List to store known face encodings
        self.known_face_names = []  # List to store known face names
        self.load_known_faces()  # Load known faces from the database

    def load_known_faces(self):
        recognized_faces = RecognizedFace.objects.all()
        for face in recognized_faces:
            encoding = pickle.loads(face.face_encoding)
            self.known_face_encodings.append(encoding)
            self.known_face_names.append(face.name)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces and get encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Check for unknown faces
        for (face_encoding, face_location) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
            else:
                # If the face is unknown, send SMS
                self.send_sms_alert()

            (top, right, bottom, left) = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def send_sms_alert(self):
        # Implement SMS sending functionality here
        import requests

        # Example using Twilio
        account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
        auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
        from_number = 'YOUR_TWILIO_PHONE_NUMBER'
        to_number = 'RECEIVER_PHONE_NUMBER'

        message = "Alert! An unrecognized person has been detected."

        # Twilio SMS API
        url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
        data = {
            'From': from_number,
            'To': to_number,
            'Body': message
        }

        response = requests.post(url, data=data, auth=(account_sid, auth_token))
        if response.status_code == 201:
            print("SMS sent successfully!")
        else:
            print("Failed to send SMS:", response.text)
