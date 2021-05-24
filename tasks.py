import math
import struct


def f11(x):
    result = math.sqrt((x ** 4 / 62 - x) / (72 * x ** 8 - 75 * x ** 3))
    result += 93 * x ** 7 + abs(x)
    result -= (x ** 5 - abs(x) + 31) / (x ** 7 / 92 + 75 * x ** 3 + 20)
    return result


def f12(x):
    if x < 144:
        return x ** 4 / 71 - x / 26
    elif 144 <= x < 190:
        return 72 * (x ** 8 - x ** 2 + 81) ** 8 - math.exp(x)
    return x ** 5 - abs(x) + 31


def f13(n, m):
    first, second = 0, 0
    for i in range(1, n + 1):
        second += math.exp(i) - 49 * i ** 7
        for j in range(1, m + 1):
            first += i ** 4 / 62 - j
    return 62 * first - 57 * second


def f14(n):
    if n:
        prev = f14(n - 1)
        return math.tan(prev) - prev ** 2 / 72 - 18
    return 5


def f21(array: list) -> int:
    def check_0(lfe: int, shell: int) -> int:
        if array[0] == 'lfe':
            return lfe
        elif array[0] == 'shell':
            return shell

    def check_2(kit: int, lfe: int, php: int) -> int:
        if array[2] == 'kit':
            return kit
        elif array[2] == 'lfe':
            return lfe
        elif array[2] == 'php':
            return php

    if array[3] == 'metal':
        return check_2(check_0(0, 1), 2, check_0(3, 4))
    elif array[3] == 'boo':
        return check_2(5, 6, check_0(7, 8))
    elif array[3] == 'logos':
        return 9


def f22(value: int) -> int:
    a = (value & 0b00000000000000000000000011111111) << 24
    b = (value & 0b00000000000000111111111100000000) << 5
    c = (value & 0b00000001111111000000000000000000) >> 18
    d = (value & 0b00000010000000000000000000000000) >> 2
    e = (value & 0b11111100000000000000000000000000) >> 19
    return a | b | c | d | e


def f23(array: list) -> list:
    def remove_empty(lst: list) -> list:
        return list(filter(lambda _item: _item, lst))

    def remove_duplicates(lst: list) -> list:
        result = []
        for _item in lst:
            if _item not in result:
                result.append(_item)
        return result

    array = remove_duplicates(array)
    for i, item_array in enumerate(array):
        array[i] = remove_empty(item_array)
    array = remove_empty(array)

    for i, item_array in enumerate(array):
        array[i][0] = str(round(float(item_array[0]), 1))
        array[i][1] = '/'.join(item_array[1].split('-')[::-1])
        for char in '()':
            array[i][2] = item_array[2].replace(char, '')
    array = list(map(list, zip(*array)))
    return array


def f31(binary_data: bytes) -> dict:
    def get_a(offset: int) -> dict:
        [a1, a2] = struct.unpack('> f H', binary_data[offset:offset + 4 + 2])
        offset += 4 + 2
        a3 = list(struct.unpack('> 4h', binary_data[offset:offset + 2 * 4]))
        offset += 4 * 2
        [a4] = struct.unpack('> q', binary_data[offset:offset + 8])
        offset += 8
        [a5, a6] = struct.unpack('> 2f', binary_data[offset:offset + 4 + 4])
        offset += 8
        [a7] = struct.unpack('> b', binary_data[offset:offset + 1])
        return {
            'A1': a1,
            'A2': get_b(a2),
            'A3': a3,
            'A4': a4,
            'A5': a5,
            'A6': a6,
            'A7': a7,
        }

    def get_b(offset: int) -> dict:
        [b1] = struct.unpack('> q', binary_data[offset:offset + 8])
        offset += 8
        b2 = get_c(offset)
        offset += 5 + 4 + 4
        [b3, b4] = struct.unpack('> i i', binary_data[offset:offset + 4 + 4])
        offset += 4 + 4
        [b5] = struct.unpack('> Q', binary_data[offset:offset + 8])
        offset += 8
        [b6_size] = struct.unpack('> H', binary_data[offset:offset + 2])
        offset += 2
        [b6_offset] = struct.unpack('> I', binary_data[offset:offset + 4])
        offset += 4
        b6 = [get_d(item) for item in struct.unpack(f'> {b6_size}H', binary_data[b6_offset:b6_offset + 2 * b6_size])]
        return {
            'B1': b1,
            'B2': b2,
            'B3': b3,
            'B4': b4,
            'B5': b5,
            'B6': b6,
        }

    def get_c(offset: int) -> dict:
        [c1] = struct.unpack('> 5s', binary_data[offset:offset + 5])
        offset += 5
        c1 = c1.decode('utf-8')
        [c2, c3] = struct.unpack('> f i', binary_data[offset:offset + 4 + 4])
        return {
            'C1': c1,
            'C2': c2,
            'C3': c3,
        }

    def get_d(offset: int) -> dict:
        [d1_size] = struct.unpack('> H', binary_data[offset:offset + 2])
        offset += 2
        [d1_offset] = struct.unpack('> I', binary_data[offset:offset + 4])
        offset += 4
        d1 = list(struct.unpack(f'> {d1_size}Q', binary_data[d1_offset:d1_offset + d1_size * 8]))
        [d2, d3] = struct.unpack(f'> I B', binary_data[offset:offset + 4 + 1])
        return {
            'D1': d1,
            'D2': d2,
            'D3': d3,
        }

    return get_a(5)


class C32:
    def __init__(self):
        self.state: C32.State = C32.A(self)

    def cast(self) -> int:
        return self.state.cast()

    def mute(self) -> int:
        return self.state.mute()

    class State:
        def __init__(self, parent):
            self.parent: C32 = parent

        def cast(self) -> int:
            raise RuntimeError

        def mute(self) -> int:
            raise RuntimeError

    class A(State):
        def cast(self) -> int:
            self.parent.state = C32.B(self.parent)
            return 0

        def mute(self) -> int:
            self.parent.state = C32.C(self.parent)
            return 1

    class B(State):
        def cast(self) -> int:
            self.parent.state = C32.C(self.parent)
            return 2

        def mute(self) -> int:
            self.parent.state = C32.D(self.parent)
            return 3

    class C(State):
        def cast(self) -> int:
            self.parent.state = C32.D(self.parent)
            return 4

    class D(State):
        def cast(self) -> int:
            self.parent.state = C32.E(self.parent)
            return 5

        def mute(self) -> int:
            self.parent.state = C32.F(self.parent)
            return 6

    class E(State):
        def cast(self) -> int:
            self.parent.state = C32.F(self.parent)
            return 7

    class F(State):
        def mute(self) -> int:
            self.parent.state = C32.C(self.parent)
            return 8
