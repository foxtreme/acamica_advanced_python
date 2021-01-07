def locales_setup(lang):
    translations = {
        ("es", "I'm a python developer"): "Yo soy un programador python",
        ("en", "Yo soy un programador python"): "I'm a python developer"
    }

    def translate(text, current_lang=lang):
        try:
            return translations[(current_lang, text)]
        except KeyError:
            return text

    return translate


def typed_property(name, expected_type):
    private_name = "_" + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError("Expected {}".format(expected_type))
        setattr(self, private_name, value)
    return prop


Integer = lambda name: typed_property(name, int)
Float = lambda name: typed_property(name, float)
String = lambda name: typed_property(name, str)


class Employee(object):
    name = String("name")
    age = Integer("age")
    salary = Float("salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "Employee('{}', {}, {}".format(self.name, self.age, self.salary)