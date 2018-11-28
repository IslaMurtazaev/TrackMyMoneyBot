from api.models import User, Message
from api.common.exceptions import EntityDoesNotExist


class UserRepo:
    def get_user_by_id(self, id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            raise EntityDoesNotExist()

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


class MessageRepo:
    def get_message_by_id(self, id):
        try:
            message = Message.objects.get(pk=id)
        except Message.DoesNotExist:
            raise EntityDoesNotExist()

        return message

    def create_message(self, id, user_id, date, text):
        message = Message()
        message.id = id
        message.user_id = user_id
        message.date = date
        message.text = text

        message.save()
        return message

