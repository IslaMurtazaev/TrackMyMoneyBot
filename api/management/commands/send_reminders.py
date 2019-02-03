from django.core.management.base import BaseCommand
from api.factories.interactors import ReminderInteractorFactory


class Command(BaseCommand):
    help = "sends a message to all active users, reminding them to report about their current day spending"

    def __init__(self):
        super().__init__()
        self.reminder_interactor = ReminderInteractorFactory.create()

    def handle(self, *args, **kwargs):
        self.reminder_interactor.execute()
