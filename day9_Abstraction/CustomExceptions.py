class SampleException(BaseException):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)