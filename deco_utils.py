from functools import wraps


def logged(func):
    print("Adding logging to ", func.__name__)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("You called the '{}' function".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


def log_format(fmt):

    def logged(func):
        print("Adding logging to ", func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return logged


def log_methods(cls):
    variables = vars(cls).items()
    for item in variables:
        if callable(item[1]):
            setattr(cls, item[0], logged(item[1]))
    return cls
