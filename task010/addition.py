# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def SumDigits(number: int):
    number = abs(number)
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


def float_digits(number: float):
    while round(number % 1, len(str(number))-1-len(str(int(number)))) > 0:
        number = round(number*10, len(str(number))-1-len(str(int(number))))
    return int(number)


numb1 = float(input("Введите вещественное число: "))

numb1 = float_digits(numb1)

sum1 = SumDigits(numb1)
print(f"Сумма цифр = {sum1}")
