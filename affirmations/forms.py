from django import forms
from .models import AudioRecording, TextAffirmations

class AudioRecordingForm(forms.ModelForm):
    class Meta:
        model = AudioRecording
        fields = ['audio_file']


class TextAffirmationsForm(forms.ModelForm):
    class Meta:
        model = TextAffirmations
        fields = [ 'message']  # Specify the fields to include in the form

    def __init__(self, *args, **kwargs):
        super(TextAffirmationsForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'class': 'form-control'})  # Add Bootstrap class 'form-control'
