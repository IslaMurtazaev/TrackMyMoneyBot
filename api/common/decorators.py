import logging


def log_exception(method):
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as ex:
            exception_message = str(ex)
            logging.exception(exception_message)
            status = 500
            return exception_message, status

    return method_wrapper
