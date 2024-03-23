from django.shortcuts import render

# Create your views here.


def profile_page(request):
    user = request.user
    context = {
        "user": user
    }
    return render(request,'myprofile/profile.html', context)