from django import forms
from django.contrib.auth.models import User
from publications.models import Album, Tag


class RedactUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'topic']

    name = forms.CharField(max_length = 255, widget = forms.TextInput(attrs = {
        'class': 'first-input',
        'placeholder': 'Настрій'
    }))

    topic = forms.SelectMultiple(
    )
