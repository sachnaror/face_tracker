import os
import pickle

import face_recognition
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from tracking.camera import VideoCamera

from .models import RecognizedFace


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def add_recognized_face(request):
    if request.method == "POST":
        directory = '/Users/homesachin/Desktop/faces'
        faces_added = []
        faces_failed = []

        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(directory, filename)
                name = os.path.splitext(filename)[0]  # Use the filename (without extension) as the name

                try:
                    # Load the image and get face encoding
                    image = face_recognition.load_image_file(image_path)
                    encodings = face_recognition.face_encodings(image)

                    if encodings:  # Check if any encodings were found
                        encoding = encodings[0]  # Take the first encoding
                        face_encoding = pickle.dumps(encoding)
                        RecognizedFace.objects.create(name=name, face_encoding=face_encoding)
                        faces_added.append(name)
                    else:
                        faces_failed.append(name)
                except Exception as e:
                    faces_failed.append((name, str(e)))

        return JsonResponse({
            'status': 'success',
            'message': 'Faces added from directory.',
            'added': faces_added,
            'failed': faces_failed
        })
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
