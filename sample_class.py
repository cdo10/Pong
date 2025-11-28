class Greeter:
    def __init__(self, default_message: str ):
        self.default_message = default_message

    def greet(self, message):
        if message is not None:
            print(message)
        else:
            print(self.default_message)
