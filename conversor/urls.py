from django.urls import path
from .views import convert_view

urlpatterns = [
    path('', convert_view, name='conversor'),
]
