from api.views.views import MessageReceiverView
from api.factories.interactors import CreateUserInteractorFactory, AuthenticateUserInteractorFactory, \
    CreateMessageInteractorFactory
from telepot import Bot
from main.settings import BOT_TOKEN


class MessageReceiverViewFactory:
    @staticmethod
    def create():
        create_user_interactor = CreateUserInteractorFactory.create()
        authenticate_user_interactor = AuthenticateUserInteractorFactory.create()
        create_message_interactor = CreateMessageInteractorFactory.create()
        bot = Bot(BOT_TOKEN)
        return MessageReceiverView(create_user_interactor, authenticate_user_interactor, create_message_interactor, bot)
