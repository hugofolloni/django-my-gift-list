from django.shortcuts import render
from gifts.models import Gift, User, Event
from gifts.forms import EventForm, UserForm, GiftForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return render(request, 'index.html')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def giftlist(request, id):
    event = Event.objects.get(id=id)
    gifts = Gift.objects.filter(event=event)
    if request.method == "POST":
        form = GiftForm(request.POST)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.event = event
            gift.save()
            gifts = Gift.objects.filter(event=event)
            return render(request, 'giftlist.html', {'form': form, 'event': event, 'gifts': gifts})
    else:
        form = GiftForm()
    return render(request, 'giftlist.html', {'form': form, 'event': event, 'gifts': gifts})

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = User.objects.get(id=1)
            event.save()
            return render(request, 'index.html')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})
