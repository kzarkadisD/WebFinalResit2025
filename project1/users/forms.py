from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    username = forms.CharField(
        max_length=10,
        help_text="Username up to 10 characters, letters and numbers only."
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        help_text="Password must be at least 8 characters, letters and numbers only."
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 10:
            raise ValidationError("Username cannot exceed 10 characters.")
        if not re.match("^[a-zA-Z0-9]*$", username):
            raise ValidationError("Username can only contain letters and numbers.")
        return username

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters.")
        if not re.match("^[a-zA-Z0-9]*$", password):
            raise ValidationError("Password can only contain letters and numbers.")
        return password