# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint

list1 = [int(input(f'Введите элемент № {i}:')) for i in range(int(input('Введите размер списка:')))]
print(list1)
k = int(input('Введите число: '))

print('Первый способ:',list1[k:]+list1[:k])

list2 = []
for i in range(len(list1)):
    list2.append(list1[k])
    k+=1
    if k == len(list1):
        k = 0
print('Второй способ:',list2)