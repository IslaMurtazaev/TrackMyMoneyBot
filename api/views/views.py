from api.common.exceptions import EntityDoesNotExist


class MessageReceiverView:
    def __init__(self, create_user_interactor, authenticate_user_interactor, create_message_interactor, handle_message_interactor):
        self.create_user_interactor = create_user_interactor
        self.authenticate_user_interactor = authenticate_user_interactor
        self.create_message_interactor = create_message_interactor
        self.handle_message_interactor = handle_message_interactor

    def post(self, **kwargs):
        if kwargs.get('edited_message') is not None:
            return '', 200

        user = self._authenticate_user(kwargs)
        message = self.create_message_interactor.set_params(user_id=user.id, **kwargs).execute()

        self.handle_message_interactor.set_params(user, message).execute()

        body = "Ok, buddy"
        status = 200
        return body, status

    def _authenticate_user(self, kwargs):
        user_attrs = kwargs['message']['from']

        try:
            user = self.authenticate_user_interactor.set_params(
                **user_attrs).execute()
        except EntityDoesNotExist:
            user = self.create_user_interactor.set_params(
                **user_attrs).execute()

        return user
