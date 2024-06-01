from django.conf import settings
from django.core.mail import send_mail
from django.core.management import BaseCommand

from mailing.models import Mailing, Message
from mailing.services import send_mailing


class Command(BaseCommand):

    def handle(self, *args, **options):
        mailing = Mailing.objects.filter(message=message)

        send_mail(
            subject=message.subject,
            message=message.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.client.all()]
        )

