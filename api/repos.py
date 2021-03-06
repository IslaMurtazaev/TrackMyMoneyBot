from datetime import datetime

from api.models import User, Message, Consumption
from api.common.exceptions import EntityDoesNotExist


class UserRepo:
    @staticmethod
    def get_user_by_id(id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            raise EntityDoesNotExist("User does not exist")

        return user

    @staticmethod
    def get_all(**kwargs):
        users = User.objects.filter(**kwargs)
        return users

    @staticmethod
    def create_user(id, first_name, last_name, is_bot, is_active):
        user = User()
        user.id = id
        user.first_name = first_name
        user.last_name = last_name
        user.is_bot = is_bot
        user.is_active = is_active

        user.save()
        return user

    @staticmethod
    def activate_user(id):
        user = User.objects.get(pk=id)
        user.is_active = True
        user.save()
        return user


class MessageRepo:
    @staticmethod
    def get_message_by_id(id):
        try:
            message = Message.objects.get(pk=id)
        except Message.DoesNotExist:
            raise EntityDoesNotExist("Message does not exist")

        return message

    @staticmethod
    def create_message(id, user_id, date, text):
        message = Message()
        message.id = id
        message.user_id = user_id
        message.date = date
        message.text = text

        message.save()
        return message


class ConsumptionRepo:
    @staticmethod
    def get_consumption_by_id(id):
        try:
            consumption = Consumption.objects.get(pk=id)
        except Consumption.DoesNotExist:
            raise EntityDoesNotExist("Consumption does not exist")

        return consumption

    @staticmethod
    def create_consumption(user_id, date, cost, comment):
        consumption = Consumption()
        consumption.user_id = user_id
        consumption.date = date
        consumption.cost = cost
        consumption.comment = comment

        consumption.save()
        return consumption

    @staticmethod
    def get_all_in_current_month(user_id):
        now = datetime.now()
        this_month_consumptions = Consumption.objects.filter(user_id=user_id,
                                                             date__year=now.year, date__month=now.month)
        return this_month_consumptions

    @staticmethod
    def get_all_in_current_day(user_id):
        now = datetime.now()
        this_day_consumptions = Consumption.objects.filter(user_id=user_id, date__year=now.year,
                                                           date__month=now.month, date__day=now.day)
        return this_day_consumptions

    @staticmethod
    def delete_last(user_id):
        try:
            last_consumption = Consumption.objects.filter(user_id=user_id).latest("date")
            last_consumption.delete()
        except Consumption.DoesNotExist:
            raise EntityDoesNotExist("Consumption does not exist")

    @staticmethod
    def delete_by_id(user_id, consumption_id):
        try:
            Consumption.objects.get(user_id=user_id, id=consumption_id).delete()
        except Consumption.DoesNotExist:
            raise EntityDoesNotExist("Consumption does not exist")

    @staticmethod
    def get_last_five(user_id):
        try:
            last_five_consumptions = Consumption.objects.filter(user_id=user_id).order_by("id")[::-1][:5]
            return last_five_consumptions
        except Consumption.DoesNotExist:
            raise EntityDoesNotExist("Consumption does not exist")

    @staticmethod
    def get_last(user_id):
        try:
            last_five_consumptions = Consumption.objects.filter(user_id=user_id).order_by("id")[::-1][0]
            return last_five_consumptions
        except Consumption.DoesNotExist:
            raise EntityDoesNotExist("Consumption does not exist")
