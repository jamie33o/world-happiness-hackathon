from django.shortcuts import render
from affirmations.models import TextAffirmations


def home_page(request):

    context = {
        "home_url": "home",
    }
    if request.user.is_authenticated:
        text_affirmation = TextAffirmations.objects.filter(user=request.user)
        context["text_affirmation"] = text_affirmation
    return render(request, "home/index.html", context)
