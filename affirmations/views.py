from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import AudioRecording, TextAffirmations
from .forms import AudioRecordingForm, TextAffirmationsForm


def affirmation_page(request):
    if request.user.is_authenticated:
        form = AudioRecordingForm()
        recordings = AudioRecording.objects.filter(user=request.user)
        return render(request, 'affirmations/affirmations.html',
                  {'form': form, 'recordings': recordings})
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

    return redirect('affirmations')


def group_affirmations(request):
    if request.method == 'POST':
        form = TextAffirmationsForm(request.POST)
        if form.is_valid():
            text_affirmation = form.save(commit=False)
            text_affirmation.user = request.user
            text_affirmation.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('group_affirmations')
        messages.error(request, 'Error could not send message')
        return redirect('group_affirmations')
    else:
        text_affirmations = TextAffirmations.objects.all()

        context = {
            'text_affirmations': text_affirmations   
            }

    return render(request,
                  'affirmations/group_affirmations.html', context)



def delete_message(request, message_id):
    message = get_object_or_404(TextAffirmations, id=message_id)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully.')
        return redirect('group_affirmations')
    messages.error(request, 'Error could not delete Message')

    return redirect('group_affirmations')

def edit_message(request, message_id):
    message = get_object_or_404(TextAffirmations, id=message_id)
    
    if request.method == 'POST':
        form = TextAffirmationsForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message updated successfully.')
            return redirect('group_affirmations')
        else:
            messages.error(request, 'Error updating message. Please check the form.')
    return redirect('group_affirmations')
