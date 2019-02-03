import re
from datetime import datetime
from django.utils import timezone
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup

from api.common.exceptions import UnsupportedContentType, EntityDoesNotExist


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


class HandleCallbackQueryInteractor:
    def __init__(self, bot, consumption_repo):
        self.bot = bot
        self.consumption_repo = consumption_repo

    def set_params(self, user=None, **kwargs):
        self.user = user
        self.data = kwargs.get("data")
        return self

    def execute(self):
        if self.data == "count_this_month":
            consumptions = self.consumption_repo.get_all_in_current_month(user_id=self.user.id)
            consumptions_sum = sum(consumption.cost for consumption in consumptions)
            self.bot.sendMessage(self.user.id, "You have spent {} money in this month".format(consumptions_sum))

        elif self.data == "count_this_day":
            consumptions = self.consumption_repo.get_all_in_current_day(user_id=self.user.id)
            consumptions_sum = sum(consumption.cost for consumption in consumptions)
            self.bot.sendMessage(self.user.id, "You have spent {} money during this day".format(consumptions_sum))

        elif self.data.startswith("remove_consumption_with_id"):
            p = re.compile("remove_consumption_with_id=(\d+)")
            m = p.match(self.data)
            consumption_id = int(m.group(1))
            try:
                self.consumption_repo.delete_by_id(user_id=self.user.id, consumption_id=consumption_id)
                self.bot.sendMessage(self.user.id, "Deleted")
            except EntityDoesNotExist:
                self.bot.sendMessage(self.user.id, "Something went wrong")


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
                self._handle_spent_command()
            elif self.message.text.startswith("/count"):
                self._handle_count_command()
            elif self.message.text.startswith("/cancel"):
                self._handle_cancel_command()
            elif self.message.text.startswith("/help"):
                self._handle_help_command()
            elif self.message.text.startswith("/"):
                self.bot.sendMessage(self.user.id, "I don't understand this command, you can use /help" +
                                     " to get a list of my avalilable commands")
        else:
            self.bot.sendMessage(
                self.user.id, 'Hello {}! Before I can track your budget, you need to activate your account'.format(
                    self.user.id)
            )

    def _handle_spent_command(self):
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

    def _handle_count_command(self):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="This month", callback_data="count_this_month")],
            [InlineKeyboardButton(text="This day", callback_data="count_this_day")],
        ])

        self.bot.sendMessage(self.user.id, "What exactly you want to count?", reply_markup=keyboard)

    def _handle_help_command(self):
        self.bot.sendMessage(self.user.id,
                             "At your service! I am here to help you log your financial spendings, so" +
                             " that you don't have to memorize it or write anything on paper)\n\n" +
                             "In case you don't know, these are the commands to ask me:\n\n" +
                             "/spent - log your spending \n(e.g. \"/spent 130 on shaurma\")\n" +
                             "/count - get a sum of all your spendings in current month/day\n" +
                             "/cancel - in case of accidentally saving a spending it can be canceled")

    def _handle_cancel_command(self):
        last_five_consumptions = self.consumption_repo.get_last_five(self.user.id)
        inline_keyboard = []
        for consumption in last_five_consumptions:
            if consumption.comment == "":
                consumption.comment = "No comment"
            inline_keyboard.append([InlineKeyboardButton(text=consumption.comment,
                                                         callback_data="remove_consumption_with_id={}".format(
                                                             consumption.id))])
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        self.bot.sendMessage(self.user.id, "Which consumption you want to cancel?", reply_markup=keyboard)


class ReminderInteractor:
    def __init__(self, user_repo, bot):
        self.user_repo = user_repo
        self.bot = bot

    def execute(self):
        active_users = self.user_repo.get_all(is_active=True)
        for user in active_users:
            self.bot.sendMessage(user.id, "Don't forget to send me your today's spending {}".format(user.first_name))
