from celery import shared_task
import time
from .services import send_test_email

# @shared_task
# def slow_add(x,y ):
#   time.sleep(5)
#   return x+y


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=10, retry_kwargs={"max_retries": 3})
def send_test_email_task(self, to_email):
  send_test_email(to_email)