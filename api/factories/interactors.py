from api.interactors import CreateUserInteractor, AuthenticateUserInteractor
from api.factories.repos import UserRepoFactory


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
