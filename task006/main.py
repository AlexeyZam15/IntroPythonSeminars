# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# проверяет вводимое число на шестизначность
while True:
    number_ticket = int(input("Введите шестизначный номер билета: "))
    if 99999 < number_ticket < 1000000:
        break
    else:
        print("Введены неверные данные")

# создаёт список из цифр числа
def digitsList(number: int):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits

# проверяет равна ли сумма элементов одной половины списка другой половине списка
def equalitySumHalvesElementsList(numbers=[]):
    size = len(numbers)
    if size % 2 == 0:
        sum = 0
        sum1 = 0
        for i in range((size)//2):
            sum += numbers[i]
            sum1 += numbers[size-i-1]
        if sum == sum1:
            return True
        else:
            return False
    else:
        return False


digits_ticket = digitsList(number_ticket)

lucky = equalitySumHalvesElementsList(digits_ticket)

print("Поздравляем, у вас счастливый билет!" if lucky else "Ваш билет не счастливый! Повезёт в следующий раз!")
