from api.repos import UserRepo, MessageRepo, ConsumptionRepo


class UserRepoFactory:
    @staticmethod
    def create():
        return UserRepo


class MessageRepoFactory:
    @staticmethod
    def create():
        return MessageRepo


class ConsumptionRepoFactory:
    @staticmethod
    def create():
        return ConsumptionRepo
