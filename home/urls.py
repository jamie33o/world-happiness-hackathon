from django.urls import path
from .views import home_page, upload_recording

urlpatterns = [
    path("", home_page, name='home'),
    path("upload_recording/", upload_recording, name='upload_recording'),

    ]