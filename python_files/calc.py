"""
Module to provide a simple calculation interface
"""


def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError("Integer only accepted")


def sub(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    else:
        raise TypeError("Integer only accepted")


def mul(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    else:
        raise TypeError("Integer only accepted")


def div(a, b):
    if a == 0:
        raise ValueError("Zero not allowed")
    elif isinstance(a, int) and isinstance(b, int):
        return a / b
    else:
        raise TypeError("Integer only accepted")
