from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from celery import shared_task
from django.contrib.auth import get_user_model
from .models import Book

logger = get_task_logger(__name__)


@shared_task
def send_email(email_address="", message=""):
    """Sends an email when the feedback form has been submitted."""
    User = get_user_model()
    users = User.objects.all()
    for user in users:
        liked_books = Book.objects.filter(like=user)
        if liked_books:
            send_mail(
                "Your LIked Books",
                f"\t{liked_books}\n\nThank you!",
                "support@example.com",
                [user.email],
                fail_silently=False,
            )


@shared_task
def sample_task():
    logger.info("The sample task just ran.")
