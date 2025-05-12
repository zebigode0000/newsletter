from django.shortcuts import render, redirect
from .forms import SubscriberForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()

            send_mail(
                subject='seja bem vindo à nossa newsletter!',
                message='Obrigado por se inscrever. Em breve você receberá noticias e atualizações do site.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
            )

            return redirect('thank_you')
    else:
        form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form})


def send_newsletter(request):
    subject = 'seu newsletter esta aqui!'
    message = 'ola estou te enviando essa parada bem maluquinha'
    recipients = [subscriber.email for subscriber in Subscriber.objects.all()]

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)
    return redirect('thank_you')

def thank_you(request):
    return render(request, 'thank_you.html')
