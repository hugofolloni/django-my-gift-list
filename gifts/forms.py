from django import forms
from django.forms import ModelForm
from gifts.models import Gift, User, Event
from django.contrib.auth.forms import UserCreationForm

class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'description', 'link', 'price']
        exclude = ['checked', 'image']

class EventForm(ModelForm):
    name = forms.CharField(max_length=255, required=False)
    date = forms.DateField(required=False)

    class Meta:
        model = Event
        fields = ['date', 'name']
        exclude = ['user']

    
class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
