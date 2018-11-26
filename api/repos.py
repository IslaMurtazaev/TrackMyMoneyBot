from api.models import User


class UserRepo:
    def get_user_by_id(self, id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Exception("entity exception")

        return user

    def create_user(self, id, first_name, last_name, is_bot, is_active):
        user = User()
        user.id = id
        user.first_name = first_name
        user.last_name = last_name
        user.is_bot = is_bot
        user.is_active = is_active

        user.save()
        return user
