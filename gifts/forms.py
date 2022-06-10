from django import forms
from django.forms import ModelForm
from gifts.models import Gift, User, Event

class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'description', 'link', 'image', 'price']

class EventForm(ModelForm):
    name = forms.CharField(max_length=255, required=False)
    date = forms.DateField(required=False)

    class Meta:
        model = Event
        fields = ['date', 'name']
        exclude = ['user']

class UserForm(ModelForm):
    name = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(max_length=255, required=False)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
