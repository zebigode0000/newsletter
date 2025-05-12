from django.shortcuts import render, redirect
from .forms import SubscriberForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Subscriber

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form})

def send_newsletter(request):
    subject = 'Sua Newsletter!'
    message = 'Aqui está a última edição da nossa newsletter.'
    recipients = [subscriber.email for subscriber in Subscriber.objects.all()]

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipients)
    return redirect('thank_you')

def thank_you(request):
    return render(request, 'thank_you.html')
