# Напишите программу, которая
# 1. Принимает на ввод последовательность чисел. 
# 2. Выведет список неповторяющихся элементов исходной последовательности.

print('Введите числа через пробел')
numbers = [int(x) for x in input().split()]

numbers_counter = dict()
for i in numbers:
    numbers_counter[i] = 0
for i in numbers:
    numbers_counter[i] +=1
# print(numbers_counter)

unique_numbers = list()

for i in numbers_counter:
    if numbers_counter[i] == 1:
        unique_numbers.append(i)

print('Неповторяющиеся числа')
print(*unique_numbers)