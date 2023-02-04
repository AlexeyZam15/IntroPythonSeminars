# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint

list1 = [randint(-1, 5) for i in range(int(input('Введите размер списка: ')))]
print(list1)

# count = 0
# for i in range(len(list1)-1):
#     if list1[i+1] > list1[i]:
#         count += 1
# print(count)

list2 = [f'{list1[i+1]} > {list1[i]}' for i in range(0, len(list1)-1) if list1[i+1] > list1[i]]
print(len(list2),end=' (')
print(*list2,sep=', ',end=')')