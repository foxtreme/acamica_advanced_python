class MyType(type):
    def __new__(meta, clsname, bases, methods):
        print("Creating: ", clsname)
        print("Bases: ", bases)
        print("Methods: ", list(methods))
        return super().__new__(meta, clsname, bases, methods)


class Point(metaclass=MyType):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


name = 'Point'
bases = (object,)


def __init__(self, x, y):
    self.x = x
    self.y = y


def move(self, dx, dy):
    self.x += dx
    self.y += dy


methods = {
    '__init__': __init__,
    'move': move
}
