from api.views.views import MessageReceiverView
from api.factories.interactors import CreateUserInteractorFactory, AuthenticateUserInteractorFactory, \
    CreateMessageInteractorFactory, HandleMessageInteractorFactory, HandleCallbackQueryInteractorFactory


class MessageReceiverViewFactory:
    @staticmethod
    def create():
        create_user_interactor = CreateUserInteractorFactory.create()
        authenticate_user_interactor = AuthenticateUserInteractorFactory.create()
        create_message_interactor = CreateMessageInteractorFactory.create()
        handle_message_interactor = HandleMessageInteractorFactory.create()
        handle_callback_query_interactor = HandleCallbackQueryInteractorFactory.create()
        return MessageReceiverView(create_user_interactor, authenticate_user_interactor, create_message_interactor,
                                   handle_message_interactor, handle_callback_query_interactor)
