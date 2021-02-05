from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def bjcards(request):
    return render(request, 'home/bjcards.html')


def bonjovi(request):
    return render(request, 'home/bonjovi.html')


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_mail = request.POST['message-mail']
        message = request.POST['message']

        # to send a mail
        send_mail(
            'This message is from' + message_name,
            message,
            message_mail,
            ['jihane.azim@gmail.com']
        )

        return render(request, 'home/contact.html',
                      {'message_name': message_name})
    else:
        return render(request, 'home/contact.html', {})
