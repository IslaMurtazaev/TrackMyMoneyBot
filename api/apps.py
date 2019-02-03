from django.apps import AppConfig
from telepot import Bot
from main.settings import BOT_TOKEN, APP_URL


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        try:
            bot = Bot(BOT_TOKEN)
            bot.setWebhook(APP_URL)
            print("bot was successfully hooked to {}".format(APP_URL))
        except Exception as ex:
            print("Bot failed to hooke to {}".format(APP_URL))
            print(ex)
