from django.urls import path
from .views import upload_recording, affirmation_page

urlpatterns = [
    path("", affirmation_page, name='affirmations'),
    path("upload_recording/", upload_recording, name='upload_recording'),
    ]