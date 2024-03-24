from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ReviewRating
from .models import Joke

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Usuwanie domyślnych komunikatów pomocy dla pola hasła
        self.fields['password1'].help_text = ''


    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

class AddJokeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddJokeForm, self).__init__(*args, **kwargs)

    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Joke name'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Joke content'}))

    class Meta:
        model = Joke
        fields = ["name", "content"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['review']