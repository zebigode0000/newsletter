from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Subscriber
from .forms import SubscriberForm  


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()

            send_mail(
                subject='Bem-vindo à nossa newsletter!',
                message="""Obrigado por se inscrever. Em breve você receberá novidades.
                
                Tem novidade fresquinha no ar! 🚀
                O Eniac preparou algo especial para você:

                ✅ material – Ex: Lançamento de produto
                ✅ matricula – Ex:  Desconto anual
                ✅ curso – : Cupons exclusivos para assinantes

                💥 E só quem está nessa lista vai ter acesso antecipado às ofertas da semana!""",

                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
            )

            return redirect('thank_you')
    else:
        form = SubscriberForm()

    return render(request, 'subscribe.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

