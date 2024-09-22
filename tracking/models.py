# tracking/models.py
from django.db import models


class RecognizedFace(models.Model):
    name = models.CharField(max_length=100)
    face_encoding = models.BinaryField()  # Store face encoding as binary data
