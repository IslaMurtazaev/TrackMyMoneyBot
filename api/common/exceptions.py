class BotException(Exception):
    def __init__(self, message):
        super().__init__(message)


class EntityDoesNotExist(BotException):
    def __init__(self, message="Entity not found"):
        super().__init__(message)


class PermissionDenied(BotException):
    def __init__(self, message="Permission denied"):
        super().__init__(message)


class UnsupportedContentType(BotException):
    def __init__(self, message="Unsupported content type"):
        super().__init__(message)
