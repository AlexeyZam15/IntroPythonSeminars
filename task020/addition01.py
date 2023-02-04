# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint


def odd_index_elements(l=list()):
    l1 = list()
    for i in range(1, len(l), 2):
        l1.append(l[i])
    return l1


list_size = int(input('Введите размер списка: '))

list1 = [randint(0, 9) for i in range(list_size)]
print(f'- {list1} ->', end=' ')

list2 = odd_index_elements(list1)
print(f'на нечётных позициях элементы:', end=' ')
print(*list2, sep=', ')
print(f'Ответ: {sum(list2)}')
