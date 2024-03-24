from django.shortcuts import render
from affirmations.models import TextAffirmations


def home_page(request):
    text_affirmation = TextAffirmations.objects.filter(user=request.user)
    return render(request, 'home/index.html', 
                  {'home_url': 'home', 'text_affirmation':text_affirmation})

