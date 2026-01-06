from django.conf import settings
from django.core.mail import send_mail

def send_test_email(to_email):
  send_mail(
    subject="Celery Test Email",
    message="This email was sent asynchronously via Celery + Redis.",
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[to_email],
    fail_silently= False
  )