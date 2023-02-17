# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint


def print_list_indexes(list0: list):
    for i in range(len(list0)):
        print(f'{i:3}', end=' ')
    print()


def print_list(list0: list):
    for i in list0:
        print(f'{i:3}', end=' ')
    print()


def range_list_indexes(list0: list, min0: int, max0: int):
    range_list_indexes0 = []
    for i in range(len(list0)):
        if min0 <= list0[i] <= max0:
            range_list_indexes0.append(i)
    return range_list_indexes0


numbers1 = [randint(-10, 10) for i in range(20)]
print_list_indexes(numbers1)
print_list(numbers1)

min1 = int(input('Введите минимум в диапазоне: '))
max1 = int(input('Введите максимум в диапазоне: '))

# range_numbers_indexes = range_list_indexes(numbers1, min1, max1)

range_numbers_indexes = [i for i in range(
    len(numbers1)) if min1 <= numbers1[i] <= max1]

print('Индексы чисел, входящих в диапазон')
print(range_numbers_indexes)
