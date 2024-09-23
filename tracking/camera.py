import pickle

import cv2
import face_recognition
import numpy as np
import requests
from config.firebase_config import bucket, db
from django.utils import timezone

from .firebase_config import bucket, db


class VideoCamera:
    def __init__(self):
        # Replace with the camera IP
        ip_camera_url = "http://45.115.190.172:8080/video"
        self.video = cv2.VideoCapture(ip_camera_url)
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()

    def load_known_faces(self):
        # Load known faces from Firebase Firestore
        known_faces = db.collection('known_faces').stream()
        for face in known_faces:
            face_data = face.to_dict()
            encoding = pickle.loads(face_data['encoding'])
            self.known_face_encodings.append(encoding)
            self.known_face_names.append(face_data['name'])

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
                # Unknown face detected, take screenshot and send SMS
                screenshot_url = self.handle_unknown_face(frame, face_location)
                self.send_sms_alert(screenshot_url)

            # Draw rectangle around face
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def handle_unknown_face(self, frame, face_location):
        # Take a screenshot and save it to Firebase Cloud Storage
        top, right, bottom, left = face_location
        face_image = frame[top:bottom, left:right]
        filename = f'unknown_{timezone.now().timestamp()}.jpg'

        # Save the screenshot locally first
        cv2.imwrite(filename, face_image)

        # Upload to Firebase Storage
        blob = bucket.blob(f'unknown_faces/{filename}')
        blob.upload_from_filename(filename)

        # Get the public URL
        blob.make_public()
        public_url = blob.public_url

        # Save record in Firestore as "unknown"
        db.collection('unknown_faces').add({
            'timestamp': timezone.now(),
            'image_url': public_url
        })

        return public_url

    def send_sms_alert(self, screenshot_url):
        # Example using Twilio to send SMS
        account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
        auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
        from_number = 'YOUR_TWILIO_PHONE_NUMBER'
        to_number = '+919560330483'  # Your phone number

        message = f"Alert! A ghost just photobombed, time to kick some ectoplasmic butt! 👻💥: {screenshot_url}"

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
