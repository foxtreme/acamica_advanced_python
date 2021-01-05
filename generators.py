import csv


def reader(filename):
    """
    Reads lines from a file
    :param filename: string, the file name
    :return: generator, the file's lines
    """
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            yield line


def parse_transaction(lines):
    """
    casts the adequate types for every element of evey line
    :param lines: generator, the file's lines
    :return: generator, the file's lines parsed
    """
    rows = csv.reader(lines)
    types = [int, str, int, str, int, str, float, str]
    converted = ([func(val) for func, val in zip(types, row)] for row in rows)
    return converted


def filter_lines(rows, func):
    """
    Filters out elements that do not fulfill the condition in func
    :param rows: generator, the file's lines
    :param func: the function to apply
    :return: generator, the file's lines
    """
    filtered = (row for row in rows if func(row))
    return filtered
