# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

def print_number_degree(number, max):
    i = 0
    number_degree = number
    while number_degree < max:
        number_degree = number**i
        i += 1
        if number_degree < max:
            print(number_degree, end=' ')


numb1 = 2
n = int(input('Введите число: '))

print_number_degree(numb1,n)
