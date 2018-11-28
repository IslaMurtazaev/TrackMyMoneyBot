from api.common.exceptions import EntityDoesNotExist


class MessageReceiverView:
    def __init__(self, create_user_interactor, authenticate_user_interactor, create_message_interactor, bot):
        self.create_user_interactor = create_user_interactor
        self.authenticate_user_interactor = authenticate_user_interactor
        self.create_message_interactor = create_message_interactor
        self.bot = bot

    def get(self, **kwargs):
        print('kwargs', kwargs)
        body = "Ok, buddy"
        status = 200
        return body, status

    def post(self, **kwargs):
        print('kwargs', kwargs)

        message_attrs = kwargs['message']
        user_attrs = message_attrs.get('from')

        try:
            user = self.authenticate_user_interactor.set_params(
                **user_attrs).execute()
            print("user", user.first_name, "is authenticated")
        except EntityDoesNotExist:
            user = self.create_user_interactor.set_params(
                **user_attrs).execute()
            print("new user", user.first_name, "is created")

        id = message_attrs.get('message_id')
        date = message_attrs.get('date')
        text = message_attrs.get('text')

        message = self.create_message_interactor.set_params(id=id, user_id=user.id, date=date, text=text).execute()
        self.bot.sendMessage(user.id, ("I hear you, you said: " + message.text))

        body = "Ok, buddy"
        status = 200
        return body, status
