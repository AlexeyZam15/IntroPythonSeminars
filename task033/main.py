# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

estimates = [int(x) for x in input().split()]
print(estimates)

def min_replace_max(list1 : list):
    max1 = max(list1)
    min1 = min(list1)
    for i in list1:
        if list1[i] == max1:
            list1[i] = min1
            
min_replace_max(estimates)
print(estimates)