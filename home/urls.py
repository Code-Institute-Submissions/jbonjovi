from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bjcards/', views.bjcards, name='bjcards'),
    path('bonjovi/', views.bonjovi, name='bonjovi'),
    path('contact/', views.contact, name='contact'),
]
