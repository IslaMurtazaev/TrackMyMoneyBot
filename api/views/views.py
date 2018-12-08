from api.common.exceptions import EntityDoesNotExist


class MessageReceiverView:
    def __init__(self, create_user_interactor, authenticate_user_interactor, create_message_interactor,
                 handle_message_interactor, handle_callback_query_interactor):
        self.create_user_interactor = create_user_interactor
        self.authenticate_user_interactor = authenticate_user_interactor
        self.create_message_interactor = create_message_interactor
        self.handle_message_interactor = handle_message_interactor
        self.handle_callback_query_interactor = handle_callback_query_interactor

    def post(self, **kwargs):
        if kwargs.get('edited_message') is not None:
            return '', 200
        elif kwargs.get('callback_query') is not None:
            callback_query = kwargs['callback_query']
            user = self._authenticate_user(callback_query['from'])
            self.handle_callback_query_interactor.set_params(user, **callback_query).execute()
            return "", 200
        else:
            user = self._authenticate_user(kwargs['message']['from'])
            message = self.create_message_interactor.set_params(user_id=user.id, **kwargs).execute()

            self.handle_message_interactor.set_params(user, message).execute()

            body = "Ok, buddy"
            status = 200
            return body, status

    def _authenticate_user(self, user_attrs):
        try:
            user = self.authenticate_user_interactor.set_params(
                **user_attrs).execute()
        except EntityDoesNotExist:
            user = self.create_user_interactor.set_params(
                **user_attrs).execute()

        return user
