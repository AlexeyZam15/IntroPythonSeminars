# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


def list_min_remainder(l=list()):
    min = round(l[0] % 1, 2)
    for i in range(1, len(l)):
        if round(l[i] % 1, 2) < min:
            min = round(l[i] % 1, 2)
    return min


def list_max_remainder(l=list()):
    max = round(l[0] % 1, 2)
    for i in range(1, len(l)):
        if round(l[i] % 1, 2) > max:
            max = round(l[i] % 1, 2)
    return max


def dif_min_max_remainder_elements(l=list()):
    return round(list_max_remainder(l) - list_min_remainder(l), 2)


list1 = [round(uniform(0, 10), 2)
         for i in range(int(input('Введите размер списка: ')))]
print(f'- {list1} => {dif_min_max_remainder_elements(list1)}')
print(f'max = {list_max_remainder(list1)}, min = {list_min_remainder(list1)}')
