from django.db import models
from django.utils import timezone
from short_link.models import AbstractTimestamp


class Image(AbstractTimestamp):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image {self.id}"
