# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint

list1 = [randint(-1,4) for i in range(int(input('Введите размер списка: ')))]
print(*list1)

print(len(set(list1)))