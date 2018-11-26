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
        self.user_repo.create_user(id=self.id, first_name=self.first_name,
                                   last_name=self.last_name, is_bot=self.is_bot, is_active=self.is_active)


class AuthenticateUserInteractor:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def set_params(self, id=None, **kwargs):
        self.id = id
        return self

    def execute(self):
        return self.user_repo.get_user_by_id(self.id)
