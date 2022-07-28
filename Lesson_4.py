"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

# from collections import defaultdict
#
#
from collections import defaultdict
from statistics import mean
#
dict_company = defaultdict(int)
qty_company = int(input('Please input companies Qty: '))

for i in range(qty_company):
    company_name = input('Please input a company name: ')
    company_profit = input('Please fill in an quarter profit via space in RUB, millions (Sample: 40 50 55 45): ')
    dict_company[company_name] = mean([int(i) for i in company_profit.split()])

average_profit = mean(dict_company.values())
max_profit = [i for i in dict_company.keys() if dict_company[i] > average_profit]
min_profit = [i for i in dict_company.keys() if dict_company[i] < average_profit]

print(f'Total average profit: {average_profit}')
print(f'Companies with profit greater than total average profit: {max_profit}')
print(f'Companies with profit less than total average profit: {min_profit}')

"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
class HexadecimalCalc:
    def __init__(self, h):
        self.hexadecimal = h

    def __add__(self, other):
        add = str(hex(int(self.hexadecimal, 16) + int(other.hexadecimal, 16)))
        return add[2:].upper()

    def __mul__(self, other):
        mul = str(hex(int(self.hexadecimal, 16) * int(other.hexadecimal, 16)))
        return mul[2:].upper()


first_hexadec = HexadecimalCalc('a2')
second_hexadec = HexadecimalCalc('c4f')
print(first_hexadec + second_hexadec)
print(first_hexadec * second_hexadec)

"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit


lst = [i for i in range(1000)]
deq_lst = deque(lst)

# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее


def append_lst(lst):
    for i in range(100):
        lst.append(i)
    return lst


def append_deq_lst(deq_lst):
    for i in range(100):
        deq_lst.append(i)
    return deq_lst

def pop_lst(lst):
    for i in range(10000):
        lst.pop(i)
    return lst


def pop_deq_lst(deq_lst):
    for i in range(10000):
        deq_lst.pop()
    return deq_lst


def extend_lst(lst, lst_2):
    for i in range(100):
        lst.extend(lst_2)
    return lst


def extend_deq_lst(deq_lst, deq_lst_2=deque()):
    for i in range(100):
        deq_lst.extend(deq_lst_2)
    return deq_lst

print(f'append_lst: {timeit("append_lst", globals=globals())}')
print(f'append_deq_lst: {timeit("append_deq_lst", globals=globals())}')
print(f'pop_lst: {timeit("pop_lst", globals=globals())}')
print(f'pop_deq_lst: {timeit("pop_deq_lst", globals=globals())}')
print(f'extend_lst: {timeit("extend_lst", globals=globals())}')
print(f'extend_deq_lst: {timeit("extend_deq_lst", globals=globals())}')

def insert_lst(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst


def appendleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.appendleft(0, i)
    return deq_lst


def popleft_lst(lst):
    for i in range(1000):
        lst.pop(i)
    return lst


def popleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.popleft()
    return deq_lst


def extendleft_lst(lst, lst_2):
    for i in range(100):
        for i in lst_2:
            lst.insert(0, i)
        return lst_2


def extendleft_deq_lst(deq_lst):
    for i in range(100):
        deq_lst.extendleft(i)
    return deq_lst
print('----------------------')
print(f'insert_lst: {timeit("insert_lst", globals=globals())}')
print(f'appendleft_deq_lst: {timeit("appendleft_deq_lst", globals=globals())}')
print(f'popleft_lst: {timeit("popleft_lst", globals=globals())}')
print(f'popleft_deq_lst: {timeit("popleft_deq_lst", globals=globals())}')
print(f'extendleft_lst: {timeit("extendleft_lst", globals=globals())}')
print(f'extendleft_deq_lst: {timeit("extendleft_deq_lst", globals=globals())}')


def el_from_lst(x):
    for i in range(len(lst)):
        lst[i] = x
    return x


def el_from_deq_lst(x):
    for i in range(len(deq_lst)):
        deq_lst[i] = x
    return x

print('----------------------')
print(f'el_from_lst: {timeit("el_from_lst", globals=globals())}')
print(f'el_from_deq_lst: {timeit("el_from_deq_lst", globals=globals())}')

# append_lst: 0.014657800000000006
# append_deq_lst: 0.013068799999999992
# pop_lst: 0.013780100000000003
# pop_deq_lst: 0.014075900000000002
# extend_lst: 0.013974699999999993
# extend_deq_lst: 0.017900100000000002

# Вывод: нет значительных отличий в срокости выволнения
# ----------------------
# insert_lst: 0.026860999999999996
# appendleft_deq_lst: 0.01492099999999999
# popleft_lst: 0.014394400000000002
# popleft_deq_lst: 0.012977500000000003
# extendleft_lst: 0.014417899999999984
# extendleft_deq_lst: 0.012281199999999992

# Вывод: операции left у дека выполняются быстрее

# ----------------------
# el_from_lst: 0.012214799999999998
# el_from_deq_lst: 0.016683999999999977

# Вывод: извлечение быстрее происходит из списка

"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def dict_fill():
    my_dict = {1: 1, 2: 2, 3: 3}


def ordered_dict_fill():
    my_ordered_dict = OrderedDict([(1, 1), (2, 2), (3, 3)])


def dict_pop():
    my_dict = {'a': 1}
    my_dict.popitem()


def ordered_dict_pop():
    my_ordered_dict = OrderedDict({'a': 1})
    my_ordered_dict.popitem()


def dict_sort():
    my_dict = {'a': 1, 'c': 3, 'b': 2}
    my_list = sorted(my_dict)


def ordered_dict_sort():
    my_dict = OrderedDict({'a': 1, 'c': 3, 'b': 2})
    my_list = sorted(my_dict)


print("dict test")
print(timeit("dict_fill()", globals = globals(), number=100000))
print(timeit("dict_pop()", globals = globals(), number=100000))
print(timeit("dict_sort()", globals = globals(), number=100000))
print("ordered dict test")
print(timeit("ordered_dict_fill()", globals = globals(), number=100000))
print(timeit("ordered_dict_pop()", globals = globals(), number=100000))
print(timeit("ordered_dict_sort()", globals = globals(), number=100000))
#
# dict test
# 0.014466800000000009
# 0.012963299999999997
# 0.032481800000000005
# ordered dict test
# 0.049329200000000004
# 0.0476415
# 0.07421069999999999


# По скорости обычный словарь работает быстрее
# Начиная с версии 3.6 применять OrderedDict не имеет смысла, данный функционаял уже реализован в обычном словаре и
# лучшую производительность.
