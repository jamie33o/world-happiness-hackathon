from django.urls import path
from .views import (
    upload_recording,
    affirmation_page,
    delete_recording,
    text_affirmations,
    delete_message,
    edit_message,
)

urlpatterns = [
    path("", affirmation_page, name="affirmations"),
    path("text_affirmations/", text_affirmations, name="text_affirmations"),
    path("upload_recording/", upload_recording, name="upload_recording"),
    path(
        "delete_recording/<int:recording_id>", delete_recording, name="delete_recording"
    ),
    path("delete_message/<int:message_id>", delete_message, name="delete_message"),
    path("edit_message/<int:message_id>", edit_message, name="edit_message"),
]
