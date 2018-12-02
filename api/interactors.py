import re
from datetime import datetime
from django.utils import timezone
from api.common.exceptions import UnsupportedContentType


class CreateUserInteractor:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self, id=None, first_name=None, last_name=None, is_bot=None,
                   is_active=False, **kwargs):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.is_bot = is_bot
        self.is_active = is_active
        return self

    def execute(self):
        self.user_repo.create_user(id=self.id, first_name=self.first_name, last_name=self.last_name,
                                   is_bot=self.is_bot, is_active=self.is_active)


class AuthenticateUserInteractor:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self, id=None, **kwargs):
        self.id = id
        return self

    def execute(self):
        return self.user_repo.get_user_by_id(self.id)


class CreateMessageInteractor:
    def __init__(self, message_repo):
        self.message_repo = message_repo

    def set_params(self, user_id=None, message=None, **kwargs):
        self.id = message.get('id')
        self.user_id = user_id
        self.date = datetime.utcfromtimestamp(message.get('date'))
        self.date = timezone.make_aware(self.date)
        self.text = message.get('text')
        return self

    def execute(self):
        self._validate(self.text)
        return self.message_repo.create_message(id=self.id, user_id=self.user_id,
                                                date=self.date, text=self.text)

    def _validate(self, text):
        if text is None:
            raise UnsupportedContentType('No text found')


class HandleMessageInteractor:
    def __init__(self, bot, consumption_repo):
        self.bot = bot
        self.consumption_repo = consumption_repo

    def set_params(self, user=None, message=None):
        self.user = user
        self.message = message
        return self

    def execute(self):
        if self.user.is_active:
            if self.message.text.startswith("/spent"):
                p = re.compile("/spent\s*(\d+)\s*(.*)")
                m = p.match(self.message.text)
                if m is not None:
                    cost = m.group(1)
                    comment = m.group(2)
                    self.consumption_repo.create_consumption(user_id=self.user.id, date=self.message.date,
                                                             cost=cost, comment=comment)
                    self.bot.sendMessage(self.user.id, "Got it!")
                else:
                    self.bot.sendMessage(self.user.id,
                                         "Didn't catch that. Please type it like this \"/spent 100 on taco\"")
        else:
            self.bot.sendMessage(
                self.user.id, ('Hello ' + self.user.first_name +
                               '! Before I can track your budget, you need to activate your account')
            )
