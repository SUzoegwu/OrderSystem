class OrderIncompleteException(Exception):
    def __init__(self, item):
        self.message = f"Unable to process: {item} is missing"
        super().__init__(self.message)

class TooManyItemsException(Exception):
    def __init__(self, item):
        self.message = (f"Unable to process: {item} cannot be ordered more than once")
        super().__init__(self.message)