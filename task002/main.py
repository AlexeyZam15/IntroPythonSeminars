# Задача 2: Найдите сумму цифр трехзначного числа.

number1 = int(input("Введите число: "))


def SumDigits(number: int):
    number = abs(number)
    sum = 0
    while number > 0:
        sum += number % 10
        number//=10
    return sum


sum1 = SumDigits(number1)
print(f"Сумма цифр = {sum1}")