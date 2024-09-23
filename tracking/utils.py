# tracking/utils.py

import cv2

from .firebase_config import get_storage_bucket


def upload_image_to_firebase(image, filename):
    bucket = get_storage_bucket()
    blob = bucket.blob(f'unknown_faces/{filename}')
    success, buffer = cv2.imencode('.jpg', image)
    if success:
        blob.upload_from_string(buffer.tobytes(), content_type='image/jpeg')
        blob.make_public()  # Make the image publicly accessible
        return blob.public_url
    return None
