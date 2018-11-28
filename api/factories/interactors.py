from api.interactors import CreateUserInteractor, AuthenticateUserInteractor, CreateMessageInteractor
from api.factories.repos import UserRepoFactory, MessageRepoFactory


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
