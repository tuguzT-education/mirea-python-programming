import sys
from typing import TextIO


def generate_groups(codes: str, counts: list[int]):
    assert len(codes) == len(counts), "Count of codes and counts must be same"
    res = []
    for code, count in zip(codes, counts):
        res += [f"{code}{i}" for i in range(1, count + 1)]
    return res


def my_print(*args, sep: str = ' ', end: str = '\n', file: TextIO = sys.stdout, flush: bool = False) -> None:
    file.write(sep.join([str(item) for item in args]))
    file.write(end)
    if flush:
        file.flush()
