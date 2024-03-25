from django.urls import path
from .views import ProfileView

urlpatterns = [
    path("myprofile/", ProfileView.as_view(), name="profile"),
]
