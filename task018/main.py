# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

n = int(input('Введите размер списка:'))
list1 = [randint(1,n) for i in range(n)]
print(list1)
x = int(input('Введите число:'))
found = False
mod = 0
while found == False:
    for i in list1:
        if i == x - mod or i == x + mod:
            print(i)
            found = True
            break
    mod +=1