class MessageReceiverView:
    def __init__(self, create_user_interactor, authenticate_user_interactor):
        self.create_user_interactor = create_user_interactor
        self.authenticate_user_interactor = authenticate_user_interactor

    def get(self, **kwargs):
        print('kwargs', kwargs)
        body = "Ok, buddy"
        status = 200
        return body, status

    def post(self, **kwargs):
        print('kwargs', kwargs)

        user_attrs = kwargs['message']['from']

        try:
            user = self.authenticate_user_interactor.set_params(
                **user_attrs).execute()
            print("user", user.first_name, "is authenticated")
        except:
            user = self.create_user_interactor.set_params(
                **user_attrs).execute()
            print("new user", user.first_name, "is created")

        body = "Ok, buddy"
        status = 200
        return body, status
