from functools import reduce
import random


def first(lst) -> list:
    return [float(val) for val in lst]


def second(lst) -> int:
    return len(set(lst))


def third(lst):
    return lst[::-1]


def fourth(value, lst) -> list:
    return [i for i, val in enumerate(lst) if val == value]


def fifth(lst):
    return reduce(lambda x, y: x + y, lst[::2])


def sixth(lst: list[str]) -> str:
    return str(max(lst, key=len))


def random_str(min_size: int, max_size: int) -> str:
    return ''.join([chr(random.randint(ord('!'), ord('~'))) for _ in range(random.randint(min_size, max_size))])
