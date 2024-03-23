from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import AudioRecording, TextAffirmations
from .forms import AudioRecordingForm, TextAffirmationsForm

@login_required
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


@login_required
def delete_recording(request, recording_id):
    recording = get_object_or_404(AudioRecording, id=recording_id)
    if request.method == 'POST':
        recording.delete()
        messages.success(request, 'Recording deleted successfully.')
        return redirect('affirmations')
    messages.error(request, 'Error could not delete recording')

    return redirect('affirmations')

@login_required
def group_affirmations(request):
    if request.method == 'POST':
        form = TextAffirmationsForm(request.POST)
        if form.is_valid():
            text_affirmation = form.save(commit=False)
            text_affirmation.user = request.user
            recording_id = request.POST.get('recording_id')  

            if recording_id:
                recording = get_object_or_404(AudioRecording, id=recording_id)
                text_affirmation.recording = recording
            text_affirmation.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('group_affirmations')
        messages.error(request, 'Error could not send message')
        return redirect('group_affirmations')
    else:
        text_affirmations = TextAffirmations.objects.all()
        recordings = AudioRecording.objects.filter(user=request.user)
        context = {
            'recordings': recordings,
            'text_affirmations': text_affirmations   
            }

    return render(request,
                  'affirmations/group_affirmations.html', context)

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(TextAffirmations, id=message_id)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Message deleted successfully.')
        return redirect('group_affirmations')
    messages.error(request, 'Error could not delete Message')

    return redirect('group_affirmations')


@login_required
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
