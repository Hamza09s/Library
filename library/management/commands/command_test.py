from django.core.management.base import BaseCommand, CommandError
from library.tasks import send_email


class Command(BaseCommand):
    help = "A description of the command"

    def handle(self, *args, **options):
        self.stdout.write("My sample command just ran.")
        send_email()
