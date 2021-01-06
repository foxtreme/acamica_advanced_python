import typed


class Employee(object):
    name = typed.String("name")
    age = typed.Integer("age")
    salary = typed.Float("salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.salary = salary
        self.age = age
