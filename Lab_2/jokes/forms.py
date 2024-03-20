from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Usuwanie domyślnych komunikatów pomocy dla pola hasła
        self.fields['password1'].help_text = ''


    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
