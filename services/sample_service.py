from myexceptions import NumberFormatError


def adding(x,y):
    if isinstance(x, str) or isinstance(y, str):
        raise NumberFormatError("No strings required here")
    return x + y