from api.views.views import MessageReceiverView
from api.factories.interactors import CreateUserInteractorFactory, AuthenticateUserInteractorFactory


class MessageReceiverViewFactory:
    @staticmethod
    def create():
        create_user_interactor = CreateUserInteractorFactory.create()
        authenticate_user_interactor = AuthenticateUserInteractorFactory.create()
        return MessageReceiverView(create_user_interactor, authenticate_user_interactor)
