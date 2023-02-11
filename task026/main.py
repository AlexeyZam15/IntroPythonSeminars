# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

a = int(input('Введите число: '))
b = int(input('Введите степень: '))


def degree_f(number, degree):

    if degree > 0:
        number *= number
        degree_f(number, degree-1)
    if degree == 0:
        return 1
    return number


print(f'{a}^{b} =', degree_f(a, b))