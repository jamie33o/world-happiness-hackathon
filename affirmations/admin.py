from django.contrib import admin
from .models import AudioRecording, TextAffirmations

# Register your models here.
admin.site.register(AudioRecording)
admin.site.register(TextAffirmations)
