from deco_utils import log_format
logged = log_format("Calling {}")

@logged
def add(x, y):
    return x + y


@logged
def sub(x, y):
    return x - y


@logged
def multiply(x, y):
    return x * y
