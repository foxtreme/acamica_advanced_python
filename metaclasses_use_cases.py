_formatters = {}


class BaseFormatter(type):
    def __init__(cls, clsname, bases, methods):
        super().__init__(clsname, bases, methods)
        if hasattr(cls, 'name'):
            _formatters[cls.name] = cls


class TextFormatter(metaclass=BaseFormatter):
    name = 'text'


class CSVFormatter(metaclass=BaseFormatter):
    name = 'csv'


class HTMLFormatter(metaclass=BaseFormatter):
    name = 'html'


def get_formatter(name):
    formatter = _formatters.get(name)
    if formatter:
        return formatter()
    else:
        raise ValueError("Unknown formatter")