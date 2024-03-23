from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import AudioRecording
from .forms import AudioRecordingForm


def affirmation_page(request):
    if request.user.is_authenticated:
        form = AudioRecordingForm()
        recordings = AudioRecording.objects.filter(user=request.user)
        return render(request, 'affirmations/affirmations.html', {'form': form, 'recordings': recordings})
    else:
        messages.add_message(
                request,
                messages.INFO,
                'Please login/register first to view this page')
    return redirect('home')


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



def delete_recording(request, recording_id):
    recording = get_object_or_404(AudioRecording, id=recording_id)

    if request.method == 'POST':
        recording.delete()
        messages.success(request, 'Recording deleted successfully.')
        return redirect('affirmations')
    messages.error(request, 'Error could not delete recording')

    return render(request, 'confirm_delete.html', {'recording': recording})
