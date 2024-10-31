from django.db import models
from django.utils.crypto import get_random_string


class AbstractTimestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Url(AbstractTimestamp):
    url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=5, unique=True, default=get_random_string(length=5))

    def __str__(self):
        return self.url
    
    def full_url(self):
        return f"https://{self.url}"
