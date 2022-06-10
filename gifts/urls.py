from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('gifts/<int:id>', views.giftlist, name='giftlist'),
    path('create_event/', views.create_event, name='create_event'),
]