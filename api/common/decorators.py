import json
import logging
from django.http import HttpResponse
from api.common.exceptions import BotException


def handle_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as ex:
            exception_message = str(ex)

            if isinstance(ex, BotException):
                print(exception_message)
                status = 200
            else:
                logging.exception(exception_message)
                status = 500

            return HttpResponse(json.dumps(exception_message), status=status, content_type='application/json')

    return method_wrapper
