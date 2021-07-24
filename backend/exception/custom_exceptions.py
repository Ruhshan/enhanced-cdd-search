
class DhandleNotFound(Exception):
    def __init__(self, message: str):
        self.message = message

class CallToNCBIFailed(Exception):
    def __init__(self, message: str):
        self.message = message

class InvalidBatchSearchId(Exception):
    def __init__(self, message: str):
        self.message = message

