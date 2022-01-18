import sys


def count_lines(file):
    with open(file, "r") as f:
        rez = len(f.readlines())
        return rez


def count_chars(file):
    with open(file, "r") as f:
        rez = f.read().replace(" ", "")
        char = 0
        for _ in rez:
            char += 1
        return char


def test(file):
    try:
        lines = count_lines(file)
        chars = count_chars(file)
        return f"{lines} lines, {chars} chars"
    except IndentationError:
        print("somthing wrong")
