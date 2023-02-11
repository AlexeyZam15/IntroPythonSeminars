# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

numb = int(input())

def prime_number(number):
    if number < 2:
        return False
    for i in range(2,int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if prime_number(numb):
    print('yes')
else:
    print('no')