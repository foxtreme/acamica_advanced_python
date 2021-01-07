from deco_utils import logged


@logged
def add(x, y):
    return x + y


@logged
def sub(x, y):
    return x - y


@logged
def multiply(x, y):
    return x * y
