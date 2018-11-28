from api.repos import UserRepo, MessageRepo


class UserRepoFactory:
    @staticmethod
    def create():
        return UserRepo()


class MessageRepoFactory:
    @staticmethod
    def create():
        return MessageRepo()
