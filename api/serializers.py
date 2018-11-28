class ExceptionSerializer:
    @staticmethod
    def serialize(exception):
        body = {
            'error': {
                'message': str(exception)
            }
        }

        return body
