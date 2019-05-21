from telepot import Bot
from main.settings import BOT_TOKEN
from api.factories.repos import UserRepoFactory, MessageRepoFactory, ConsumptionRepoFactory
from api.interactors import CreateUserInteractor, AuthenticateUserInteractor, CreateMessageInteractor, \
    HandleMessageInteractor, HandleCallbackQueryInteractor, ReminderInteractor


class CreateUserInteractorFactory:
    @staticmethod
    def create():
        user_repo = UserRepoFactory.create()
        return CreateUserInteractor(user_repo)


class AuthenticateUserInteractorFactory:
    @staticmethod
    def create():
        user_repo = UserRepoFactory.create()
        return AuthenticateUserInteractor(user_repo)


class CreateMessageInteractorFactory:
    @staticmethod
    def create():
        message_repo = MessageRepoFactory.create()
        return CreateMessageInteractor(message_repo)


class HandleMessageInteractorFactory:
    @staticmethod
    def create():
        bot = Bot(BOT_TOKEN)
        consumption_repo = ConsumptionRepoFactory.create()
        user_repo = UserRepoFactory.create()
        return HandleMessageInteractor(bot, consumption_repo, user_repo)


class HandleCallbackQueryInteractorFactory:
    @staticmethod
    def create():
        bot = Bot(BOT_TOKEN)
        consumption_repo = ConsumptionRepoFactory.create()
        return HandleCallbackQueryInteractor(bot, consumption_repo)


class ReminderInteractorFactory:
    @staticmethod
    def create():
        user_repo = UserRepoFactory.create()
        bot = Bot(BOT_TOKEN)
        return ReminderInteractor(user_repo, bot)
