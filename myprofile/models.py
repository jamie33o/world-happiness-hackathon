from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom User model extending AbstractUser.

    Fields:
    - profile_image (ImageField): User's profile image.
    - date_of_birth (DateField): User's date of birth.
    """

    profile_image = models.ImageField(upload_to='profile_images/',
                                      null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
