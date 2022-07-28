"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit
from cProfile import run

my_list = [i for i in range(1000)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# Оптимизируем функцию применив list comprehensions
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr



def func_time_compare(func_1, func_2):

    res_1 = timeit("func_1(my_list)", globals=globals(), number=1)
    print(res_1)
    res_2 = timeit("func_2(my_list)", globals=globals(), number=1)
    print(res_2)
    return  ((res_1 - res_2) / res_1) * 100

print(f'Разница во времени между первым и вторым вариантом составляет {func_time_compare(func_1, func_2):.2f} %')


#
# Вывод: Применив list comprehension удалось увеличить скорость работы функции примерно на 10-20%.
# 6.969999999999893e-05
# 5.8000000000002494e-05
# Разница во времени между первым и вторым вариантом составляет 16.79 %

"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',

        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

# Мемоизация не имеет смысла, т.к. обертываемая функция будет вызвана всего один раз.

"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit

numbers = 123456789

# Самый медленный вариант ~ 0,17 сек

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

# Средний вариант по длительности ~ 0,11 сек

def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# Самый быстрый из трех вариантов при помоще среза ~ 0,02 сек

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

# Вариант 4 при помощи reversed. Третий по скорости из четырех ~ 0,06 сек, но зато самый компактный и элегантный.

def revers_4(enter_num):
    revers_num = ''.join(reversed(str(enter_num)))
    return int(revers_num)

# Вариант 5 через цикл for. ~ 0,08 сек.

def revers_5(enter_num):
    reversed_lst = ''
    for i in str(enter_num):
        reversed_lst = i + reversed_lst
    return int(reversed_lst)


print(timeit('revers(numbers)', globals=globals(), number=100000))
print(timeit('revers_2(numbers)', globals=globals(), number=100000))
print(timeit('revers_3(numbers)', globals=globals(), number=100000))
print(timeit('revers_4(numbers)', globals=globals(), number=100000))
print(timeit('revers_5(numbers)', globals=globals(), number=100000))

"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit
from collections import Counter


array = [1, 3, 1, 3, 4, 5, 1]

# Функция 1. Время 0,08 сек - быстрее чем вариант 2
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

# Функция 1. Время 0,12 сек  - медленее чем вариант 1 т.к. идет наполнение массива новыми значениями,
# из которых потом находим максимальное значение.
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

# Самый быстрый вариант к тому же с элегантным кодом. Функция MAX для массива с ключом по кол-ву - 0,06 сек.

def func_3():
    return max(array, key=array.count)

print(timeit('func_1()', globals=globals(), number=100000))
print(timeit('func_2()', globals=globals(), number=100000))
print(timeit('func_3()', globals=globals(), number=100000))
