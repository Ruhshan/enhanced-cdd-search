
class DhandleNotFound(Exception):
    pass

class CallToNCBIFailed(Exception):
    def __init__(self, message: str):
        self.message = message
