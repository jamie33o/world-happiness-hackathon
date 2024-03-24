from django.db import models
from django.contrib.auth import get_user_model


class AudioRecording(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, default='audio')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio_recordings/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 


class TextAffirmations(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.CharField(max_length=254, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    