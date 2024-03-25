from django import forms
from .models import CustomUser


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Fields:
    - first_name (CharField): User's first name.
    - last_name (CharField): User's last name.
    - username (CharField): User's username.
    - email (EmailField): User's email address.
    - profile_image (ImageField): User's profile image.
    - date_of_birth (DateField): User's date of birth.
    """

    class Meta:
        """
        Meta class for ProfileUpdateForm.

        Specifies the model and fields to be included in the form.
        """

        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "profile_image",
        ]
