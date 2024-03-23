from django.urls import path
from .views import upload_recording, affirmation_page, delete_recording

urlpatterns = [
    path("", affirmation_page, name='affirmations'),
    path("upload_recording/", upload_recording, name='upload_recording'),
    path("delete_recording/<int:recording_id>", delete_recording, name='delete_recording'),
]