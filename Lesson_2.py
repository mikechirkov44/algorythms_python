"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import time
import random

my_list = []
my_dict = {}

# функция декоратор для замера времени выполнения


def timing(f):
    def wrapper(*args):
        start_time = time.time()
        res = f(*args)
        stop_time = time.time()
        print('%sfunction took %0.1f ms' % (f.__name__, (stop_time-start_time) * 1000))
    return wrapper

#Пункт А - сравниваваем наполнение списка и словаря

@timing
def list_filling(massive, num):  # O(n)
    for i in range(num):  # O(n)
        massive.append(i)  # O(1)

@timing
def dict_filling(massive, num):  # O(n)
    for i in range(num):  # O(n)
        massive[i] = i  # O(1)
#
#
print(list_filling(my_list, 100000))
print(dict_filling(my_dict, 100000))
print('Несмотря на одинаковую сложность функции наполнения, словарь заполняется медленнее, \n'
'т.к. у словаря помимо заполнения генерируется хэш')

#Пункт B - сравниваваем чтение списка и словаря

@timing
def list_reading(massive):
    for i in massive: #O(n)
        print(i)  #O(1)
    return massive

@timing
def dict_reading(dictionary):
    for key in dictionary:  # O(n)
        print(dictionary[key])  # O(1)
    return dictionary

print(list_reading(my_list))
print(dict_reading(my_dict))
print('Несмотря на одинаковую сложность функции чтения, скорость считывания данных со словаря быстрее')


# Пункт С - сравнивание скорости удаления

@timing
def dict_pop(dictionary):
    for i in range(10000):    # O(n)
        dictionary.popitem()           # O(1)
    return dictionary


@timing
def list_pop(massive):
    for i in range(len(massive)):   # O(n)
        massive.pop(0)              # O(n)
    return massive


print(list_pop(my_list))
print(dict_pop(my_dict))
print('Удаление элементов словаря происходит быстрее чем у списков')

"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import hashlib
import uuid

password = input('Введите пароль: ')
salt = str(uuid.uuid4())
res = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
print(f'Хэш пароля:{res}')


with open('password.json', 'w')as f:
    f.write(f'user_1 - {res}')

with open('password.json', 'r')as f:
    pass_check = input('Введите пароль еще раз для проверки: ')
    user_pass = f.read()
    if user_pass[9:] == hashlib.sha256(salt.encode() + pass_check.encode('utf-8')).hexdigest():
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неправильный пароль')
"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib

#Функция для подсчета кол-ва уникальных подстрок в строке
def unique_substring(str):
    unique_hashes = set()
    for i in range(0, len(str)):
        for j in range(i + 1, len(str) + 1):
            sub_str = str[i:j]
            unique_hashes.add(hashlib.sha256(sub_str.encode()).hexdigest())
    print(f'Кол-во уникальных подстрок в строке "{str}" :  {len(unique_hashes)-1}')

unique_substring('papa')
unique_substring('parapam')
unique_substring('rampa')

"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib
import uuid

# Вариант решение через функцию
cache_dict = {}
salt = str(uuid.uuid4())

def cache_url(url):
    if url in cache_dict.keys():
        print(f'{url} уже имеется в кэше, Хэш страницы: {cache_dict[url]}')
    else:
        cache_dict[url] = hashlib.sha512(url.encode() + salt.encode()).hexdigest()
        print(f'Для страницы {url} записан хэш {cache_dict[url]}')
    return cache_dict

cache_url('gb.ru')
cache_url('gb.ru')
cache_url('youtube.com')
