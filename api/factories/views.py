from api.views.views import GreetingView


class GreetingViewFactory:
    @staticmethod
    def create():
        return GreetingView()
