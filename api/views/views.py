from api.common.exceptions import EntityDoesNotExist


class MessageReceiverView:
    def __init__(self, create_user_interactor, authenticate_user_interactor, create_message_interactor, bot):
        self.create_user_interactor = create_user_interactor
        self.authenticate_user_interactor = authenticate_user_interactor
        self.create_message_interactor = create_message_interactor
        self.bot = bot

    def post(self, **kwargs):
        try:
            message_attrs = kwargs['message']
        except KeyError:
            return "", 200

        user_attrs = message_attrs.get('from')

        user = self._authenticate_user(user_attrs)

        id = message_attrs.get('message_id')
        date = message_attrs.get('date')
        text = message_attrs.get('text')

        message = self.create_message_interactor.set_params(
            id=id, user_id=user.id, date=date, text=text).execute()

        if user.is_active:
            self.bot.sendMessage(
                user.id, ("I hear you, you said: " + message.text)
            )
        else:
            self.bot.sendMessage(
                user.id, ("Hello " + user.first_name +
                          "! Before I can track your budget, you need to activate your account")
            )

        body = "Ok, buddy"
        status = 200
        return body, status

    def _authenticate_user(self, user_attrs):
        try:
            user = self.authenticate_user_interactor.set_params(
                **user_attrs).execute()
            print("user", user.first_name, "is authenticated")
        except EntityDoesNotExist:
            user = self.create_user_interactor.set_params(
                **user_attrs).execute()
            print("new user", user.first_name, "is created")

        return user
