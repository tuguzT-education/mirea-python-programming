import random
import sys
from typing import TextIO

container = [
    [
        'Коллеги,',
        'В то же время,',
        'Однако,',
        'Тем не менее,',
        'Следовательно,',
        'Соответственно,',
        'Вместе с тем,',
        'С другой стороны,',
    ],
    [
        'парадигма цифровой экономики',
        'контекст цифровой трансформации',
        'диджитализация бизнес-процессов',
        'прагматичный подход к цифровым платформам',
        'совокупность сквозных технологий',
        'программа прорывных исследований',
        'ускорение блокчейн-транзакций',
        'экспоненциальный рост Big Data',
    ],
    [
        'открывает новые возможности для',
        'выдвигает новые требования',
        'несёт в себе риски',
        'расширяет горизонты',
        'заставляет искать варианты',
        'не оставляет шанса для',
        'повышает вероятность',
        'обостряет проблему',
    ],
    [
        'дальнейшего углубления',
        'бюджетного финансирования',
        'синергетического эффекта',
        'компрометации конфиденциальных',
        'универсальной коммодитизации',
        'несанкционированной кастомизации',
        'нормативного регулирования',
        'практического применения',
    ],
    [
        'знаний и компетенций.',
        'непроверенных гипотез.',
        'волатильных активов.',
        'опасных экспериментов.',
        'государственно-частных партнёрств.',
        'цифровых следов граждан.',
        'нежелательных последствий.',
        'внезапных открытий.',
    ]
]


def generate_doc() -> str:
    lst = []
    for _ in range(random.randint(1, 5)):
        lst_t = []
        for __ in range(3):
            for item in container:
                rand = random.randint(0, len(item) - 1)
                lst_t.append(item[rand])
        lst.append(' '.join(lst_t))
    return '\n\n'.join(lst)


def my_print(*args, sep: str = ' ', end: str = '\n', file: TextIO = sys.stdout, flush: bool = False) -> None:
    file.write(sep.join([str(item) for item in args]))
    file.write(end)
    if flush:
        file.flush()


def parse_subj(title: str):
    pass