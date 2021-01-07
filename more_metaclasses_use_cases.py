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
    cls._attributes = set()
    for key, value in vars(cls).items():
        if isinstance(value, Typed):
            value.name = key
            cls._attributes.add(key)
    return cls


class StructureType(type):
    def __new__(meta, name, bases, methods):
        cls = super().__new__(meta, name, bases, methods)
        return typed(cls)


class BaseStructure(metaclass=StructureType):
    def __setattr__(self, key, value):
        if key not in self._attributes:
            raise AttributeError("No attribute '{}' is allowed".format(key))
        super().__setattr__(key, value)


class Employee(BaseStructure):
    name = String()
    age = Integer()
    salary = Float()

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
