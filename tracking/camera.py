import logging
import os
import pickle
from time import time

import cv2
import face_recognition
import numpy as np
import requests

from .models import RecognizedFace

# Configure logging
logging.basicConfig(level=logging.INFO)

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()
        self.last_alert_time = 0  # Track the last time an alert was sent
        self.alert_cooldown = 30  # Cooldown period in seconds

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

        for (face_encoding, face_location) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
                color = (0, 255, 0)  # Green for known faces
            else:
                color = (0, 0, 255)  # Red for unknown faces
                current_time = time()
                if current_time - self.last_alert_time > self.alert_cooldown:
                    self.send_sms_alert()
                    self.last_alert_time = current_time  # Update the last alert time

            (top, right, bottom, left) = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), color, 8)  # Change border thickness to 8 px
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def send_sms_alert(self):
        try:
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            from_number = os.getenv('TWILIO_PHONE_NUMBER')
            to_number = os.getenv('RECEIVER_PHONE_NUMBER')

            message = "Alert! An unrecognized person has been detected."
            url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
            data = {
                'From': from_number,
                'To': to_number,
                'Body': message
            }

            response = requests.post(url, data=data, auth=(account_sid, auth_token))
            if response.status_code == 201:
                logging.info("SMS sent successfully!")
            else:
                logging.error("Failed to send SMS: %s", response.text)
        except Exception as e:
            logging.error("Error sending SMS: %s", str(e))
