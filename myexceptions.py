class NumberFormatError(Exception):
    def __init__(self, value):
        self.args = value

    def __str__(self):
        return repr(self.value)
