from deco_utils import log_methods, logged


@log_methods
class Spam(object):
    def __init__(self, value):
        self.value = value

    def yow(self):
        print("Yow!")

    def grok(self):
        print("Grok!")


class Typed(object):

    expected_type = object

    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("'{}' must be {}".format(self.name, self.expected_type))
        instance.__dict__[self.name] = value


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


def typed(cls):
    for key, value in vars(cls).items():
        if isinstance(value, Typed):
            value.name = key
    return cls


def validate(**kwargs):
    def decorate(cls):
        for name, val in kwargs.items():
            setattr(cls, name, val(name))
        return cls
    return decorate


@validate(name=String, age=Integer, salary=Float)
class Employee(object):

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
