from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    checked = models.BooleanField(default=False)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")
    date = models.DateField()

