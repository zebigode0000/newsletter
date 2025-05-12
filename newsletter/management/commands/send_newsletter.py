from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from newsletter.models import Subscriber  # ajuste o nome do app se necessário

class Command(BaseCommand):
    help = 'Envia a newsletter para todos os inscritos'

    def handle(self, *args, **kwargs):
        subject = '🗞️ Sua Newsletter chegou!'
        message = 'Olá! Aqui está a edição mais recente da nossa newsletter. Aproveite!'
        from_email = settings.DEFAULT_FROM_EMAIL

        recipients = [s.email for s in Subscriber.objects.all()]

        if not recipients:
            self.stdout.write(self.style.WARNING("Nenhum inscrito encontrado."))
            return

        send_mail(subject, message, from_email, recipients)

        self.stdout.write(self.style.SUCCESS(f"Newsletter enviada para {len(recipients)} inscritos."))
