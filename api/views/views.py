

class GreetingView:
    def get(self, **kwargs):
        body = "Hello world from api!"
        status = 200
        return body, status
