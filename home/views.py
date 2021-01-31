from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def bjcards(request):
    return render(request, 'home/bjcards.html')


def bonjovi(request):
    return render(request, 'home/bonjovi.html')


def contact(request):
    return render(request, 'home/contact.html')
