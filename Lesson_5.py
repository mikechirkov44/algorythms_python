"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта
"""
from memory_profiler import memory_usage

def mem(func):
    def wrapper(*args):
        start = memory_usage()
        res = func(args[0])
        stop = memory_usage()
        memory = stop[0] - start[0]
        return res, memory
    return wrapper

@mem
def get_profit_1(dictionary: dict):
    res = []  # O(1)
    for i in dictionary.items():  # O(n)
        res.append(i)  # O(1)
    res.sort(key=lambda x: (x[1], x[0]), reverse=True)  # O(NlogN)
    return res[0:3]

@mem
def new_get_profit(dictionary: dict):
    c_data = dictionary.copy()
    res = []
    for i in range(3):
        res.append(max(c_data, key=c_data.get))
        yield c_data.pop(res[i])
    del c_data
    del res

if __name__ == '__main__':
    test_dict = {i: i ** 3 for i in range(10000)}
    f_1, res_1 = get_profit_1(test_dict)
    g_1, res_2 = new_get_profit(test_dict)
    print(f' оригинальное решение заняло: {res_1} mib')
    print(f' отимизированное решение заняло: {res_2} mib')

 # оригинальное решение заняло: 0.8203125 mib
 # отимизированное решение заняло: 0.0 mib
# yield не хранит результат


from memory_profiler import profile

@profile
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

@profile
def new_func(n):
    new_list = filter(lambda x: x % 2 == 0, range(len(n)))
    return new_list

if __name__ == '__main__':
    a = list(range(100000))
    func_2(a)
    new_func(a)

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     35     32.0 MiB     32.0 MiB           1   @profile
#     36                                         def func_2(nums):
#     37     33.8 MiB  -2515.8 MiB      100003       new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
#     38     33.8 MiB      0.0 MiB           1       return new_arr


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     40     32.2 MiB     32.2 MiB           1   @profile
#     41                                         def new_func(n):
#     42     32.2 MiB      0.0 MiB           1       new_list = filter(lambda x: x % 2 == 0, range(len(n)))
#     43     32.2 MiB      0.0 MiB           1       return new_list

from sys import getsizeof
from collections import namedtuple

def num_translate(eng_num):
    vocablurary = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    print(f'Размер словаря {getsizeof(num_translate)}')

    print(f'{vocablurary.get(eng_num, "такого слова нет")}')


def new_func(number):
    translate_ = namedtuple('translate_', 'one, two, three, four, five,'
                                          'six, seven, eight, nine, ten')
    trl = translate_(one='один', two='два', three='три',
                     four='четыре', five='пять', six='шесть', seven='семь',
                     eight='восемь', nine='девять', ten='десять')
    print(f' Размер именованого кортежа {getsizeof(trl)}')
    return f'{getattr(trl, number.lower(), "Такой цыфры нет")}'


if __name__ == '__main__':
    num_translate('six')
    print(new_func('six'))
#
# Размер словаря 136
# шесть
#  Размер именованого кортежа 120
# шесть

import numpy
from memory_profiler import profile

@profile
def func():
    arr = [i for i in range(1, 1000000, 2)]
    return arr

# Вариант оптимизации через numpy
@profile
def new_func():
    arr = numpy.arange(1, 1000000, 2)
    return arr


if __name__ == '__main__':
    func()
    new_func()

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     36     39.9 MiB     39.9 MiB           1   @profile
#     37                                         def func():
#     38     59.2 MiB  -3478.1 MiB      500003       arr = [i for i in range(1, 1000000, 2)]
#     39     59.2 MiB      0.0 MiB           1       return arr

from memory_profiler import profile
import random
from pympler.asizeof import asizeof


@profile
def original(number: int) -> list:
    nouns = ("автомобиль", "лес", "огонь", "город", "дом")
    adverbs = ("сегодня", "вчера", "завтра", "позавчера", "ночью")
    adjectives = ("веселый", "яркий", "зеленый", "утопичный", "мягкий")
    result = []
    i = 0
    while i != number:
        joke = ' '.join((random.choice(nouns), random.choice(adverbs), random.choice(adjectives)))
        result.append(joke)
        i += 1
    del nouns
    del adverbs
    del adjectives
    del i
    return result


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


@profile
def optimize(num):
    jokes = []
    for i in range(num):
        cur_noun = random.choice(nouns)
        cur_adverb = random.choice(adverbs)
        cur_adjective = random.choice(adjectives)
    jokes.append(f'{cur_noun} {cur_adverb} {cur_adjective}')
    return jokes


if __name__ == '__main__':
    print(asizeof(original(5)))
    del original
    print(asizeof(optimize(5)))
    del optimize


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     39     40.3 MiB     40.3 MiB           1   @profile
#     40                                         def original(number: int) -> list:
#     41     40.3 MiB      0.0 MiB           1       nouns = ("автомобиль", "лес", "огонь", "город", "дом")
#     42     40.3 MiB      0.0 MiB           1       adverbs = ("сегодня", "вчера", "завтра", "позавчера", "ночью")
#     43     40.3 MiB      0.0 MiB           1       adjectives = ("веселый", "яркий", "зеленый", "утопичный", "мягкий")
#     44     40.3 MiB      0.0 MiB           1       result = []
#     45     40.3 MiB      0.0 MiB           1       i = 0
#     46     40.3 MiB      0.0 MiB           6       while i != number:
#     47     40.3 MiB      0.0 MiB           5           joke = ' '.join((random.choice(nouns), random.choice(adverbs), random.choice(adjectives)))
#     48     40.3 MiB      0.0 MiB           5           result.append(joke)
#     49     40.3 MiB      0.0 MiB           5           i += 1
#     50     40.3 MiB      0.0 MiB           1       del nouns
#     51     40.3 MiB      0.0 MiB           1       del adverbs
#     52     40.3 MiB      0.0 MiB           1       del adjectives
#     53     40.3 MiB      0.0 MiB           1       del i
#     54     40.3 MiB      0.0 MiB           1       return result
#
#
# 704
##
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     62     40.3 MiB     40.3 MiB           1   @profile
#     63                                         def optimize(num):
#     64     40.3 MiB      0.0 MiB           1       jokes = []
#     65     40.3 MiB      0.0 MiB           6       for i in range(num):
#     66     40.3 MiB      0.0 MiB           5           cur_noun = random.choice(nouns)
#     67     40.3 MiB      0.0 MiB           5           cur_adverb = random.choice(adverbs)
#     68     40.3 MiB      0.0 MiB           5           cur_adjective = random.choice(adjectives)
#     69     40.3 MiB      0.0 MiB           1       jokes.append(f'{cur_noun} {cur_adverb} {cur_adjective}')
#     70     40.3 MiB      0.0 MiB           1       return jokes
#
#
# 208

#Использование генератора впозволило сократить объем памяти в 3,5 раза.

"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""


from memory_profiler import profile
# Обернем функцию с рекурсией для получения замера

@profile
def number_reverse(num):
    if num < 10:
        return num
    else:
        return str(num % 10) + str(number_reverse(num // 10))

if __name__ == '__main__':
    number_reverse(2348972389751892735)


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     17     28.1 MiB     28.1 MiB          19   @profile
#     18                                         def number_reverse(num):
#     19     28.1 MiB      0.0 MiB          19       if num < 10:
#     20     28.1 MiB      0.0 MiB           1           return num
#     21                                             else:
#     22     28.1 MiB      0.0 MiB          18           return str(num % 10)
