from api.repos import UserRepo


class UserRepoFactory:
    @staticmethod
    def create():
        return UserRepo()
