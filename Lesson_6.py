"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit

""" Исходная функция """
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


""" Доработаная функция c реверсом """
def bubble_sort_reverse(lst: list)-> list:

    cycle = True
    while cycle:
        cycle = False
        for index in range(len(lst)-1):
            if lst[index] < lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
                cycle = True
    #print(lst)
    return lst



if __name__ == "__main__":
    for list_size in (10, 100, 1000):
        lst = [randint(-10000, 10000) for _ in range(list_size)]
        print(f'bubble_sort on {list_size} elements: {timeit("bubble_sort(lst[:])", globals=globals(), number=100)}s')
        print(f'bubble_sort_reverse on {list_size} elements: {timeit("bubble_sort_reverse(lst[:])", globals=globals(), number=100)}s')
        lst_second = [randint(-100, 100) for _ in range(list_size)]
        print(f'bubble_sort on {list_size} elements: {timeit("bubble_sort(lst_second[:])", globals=globals(), number=100)}s')
        print(f'bubble_sort_reverse on {list_size} elements: {timeit("bubble_sort_reverse(lst_second[:])", globals=globals(), number=100)}s')

# Замеры в диапозоне -10000....10000:
# bubble_sort on 10 elements: 0.0005706000000000044s
# bubble_sort_reverse on 10 elements: 0.0007238999999999995s

# bubble_sort on 100 elements: 0.0386571s
# bubble_sort_reverse on 100 elements: 0.051659s

# bubble_sort on 1000 elements: 4.72513s
# bubble_sort_reverse on 1000 elements: 7.402758399999999s

# Замеры в диапозоне -100....100:
# bubble_sort on 10 elements: 0.0005865000000000037s
# bubble_sort_reverse on 10 elements: 0.0005145000000000011s

# bubble_sort on 100 elements: 0.04417399999999999s
# bubble_sort_reverse on 100 elements: 0.05964019999999998s

# bubble_sort on 1000 elements: 4.837122499999998s
# bubble_sort_reverse on 1000 elements: 8.1066511s

#Доработка не помогла, исходная функция работает быстрее.

"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from timeit import timeit
from random import randint


def median(lst, m):
    n, i = len(lst), 0
    while True:
        if i + 1 == n:
            break
        if lst[i+1] >= lst[i]:
            i += 1
        else:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return lst[m], lst

med = 5
my_list = [randint(-100, 100) for _ in range(2 * med + 1)]
print(timeit('median(my_list, med)', globals=globals(), number=1000))

med = 50
my_list2 = [randint(-100, 100) for _ in range(2 * med + 1)]
print(timeit('median(my_list2, med)', globals=globals(), number=1000))

med = 500
my_list3 = [randint(-100, 100) for _ in range(2 * med + 1)]
print(timeit('median(my_list3, med)', globals=globals(), number=1000))

# 0.0008614000000000017
# 0.007965
# 0.1740095



from timeit import timeit
from random import randint


def median(lst):
    for i in range(len(lst)//2):
        lst.remove(max(lst))
    return max(lst)


my_list = [randint(-100, 100) for _ in range(2 * 5 + 1)]
print(timeit('median(my_list)', globals=globals(), number=1000))

my_list2 = [randint(-100, 100) for _ in range(2 * 50 + 1)]
print(timeit('median(my_list2)', globals=globals(), number=1000))

my_list3 = [randint(-100, 100) for _ in range(2 * 500 + 1)]
print(timeit('median(my_list3)', globals=globals(), number=1000))

# 0.0002898999999999992
# 0.00035480000000000234
# 0.006455699999999998




from timeit import timeit
from random import randint
from statistics import median


def find_median(lst):
    return median(lst)


my_list = [randint(-100, 100) for _ in range(2 * 5 + 1)]
print(timeit('find_median(my_list)', globals=globals(), number=1000))

my_list2 = [randint(-100, 100) for _ in range(2 * 50 + 1)]
print(timeit('find_median(my_list2)', globals=globals(), number=1000))

my_list3 = [randint(-100, 100) for _ in range(2 * 500 + 1)]
print(timeit('find_median(my_list3)', globals=globals(), number=1000))

# 0.0006062999999999902
# 0.003935900000000006
# 0.0597076

# Вывод - самое оптимальное решение во втором случае.
