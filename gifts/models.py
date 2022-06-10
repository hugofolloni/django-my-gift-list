from django.db import models

# Create your models here.

class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    image = models.URLField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")
    date = models.DateField()
    gifts = models.ManyToManyField(Gift)