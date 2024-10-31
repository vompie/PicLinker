from django.urls import path
from .views import upload_image, view_image, api_upload_image, list_images

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('images/', list_images, name='list_images'),
    path('images/<int:image_id>/', view_image, name='view_image'),
    path('api/upload/', api_upload_image, name='api_upload_image'),
]
