from django.urls import path
from .views import create_url, url_list, redirect_url


urlpatterns = [
    path('', create_url, name='create_url'),
    path('urls/', url_list, name='url_list'),
    path('<str:short_url>/', redirect_url, name='redirect_url')
]
