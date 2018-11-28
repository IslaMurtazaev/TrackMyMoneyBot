from api.serializers import ExceptionSerializer


def handle_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as ex:
            body = ExceptionSerializer.serialize(ex)
            status = 500
            print(body)
            return body, status

    return method_wrapper
