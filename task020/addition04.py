# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def number_to_binary_list(number: int):
    bin_number = list()
    while number > 1:
        bin_number.append(round(number % 2, 1))
        number //= 2
    bin_number.append(number)
    bin_number.reverse()
    return bin_number


def list_to_number(l: list):
    number = 0
    for i in range(len(l)):
        number += l[i] * 10**(len(l)-i-1)
    return number


def number_to_binary(number: int):
    return list_to_number(number_to_binary_list(number))


numb1 = int(input('Введите число: '))

print(number_to_binary(numb1))

# print(format(numb1, 'b'))
