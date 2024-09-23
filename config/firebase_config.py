import firebase_admin
from firebase_admin import credentials, firestore, storage

# Path to your Firebase Admin SDK JSON file
cred = credentials.Certificate("/Users/homesachin/Desktop/zoneone/practice/face_tracker/config/firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'wer345345c4ertwtr.appspot.com'  # Firebase Storage bucket
})

# Firestore and storage references
db = firestore.client()
bucket = storage.bucket()
