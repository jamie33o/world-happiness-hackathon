from django.http import JsonResponse
from django.shortcuts import render
from .forms import AudioRecordingForm
from django.views.decorators.csrf import csrf_exempt
from .models import AudioRecording

def affirmation_page(request):
    form = AudioRecordingForm()
    recordings = AudioRecording.objects.filter(user=request.user)

    return render(request, 'affirmations/affirmations.html',
                  {'form': form, 'recordings': recordings})

@csrf_exempt
def upload_recording(request):
    try:
        if request.method == 'POST':

            form = AudioRecordingForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.user = request.user
                # Process the uploaded file
                recording = form.save()
                return JsonResponse({'success': True, 'id': recording.id})
            else:
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)
    except Exception as e:
        print(e)