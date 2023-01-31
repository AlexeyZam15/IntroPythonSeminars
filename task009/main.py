# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120 

n = int(input('Введите целое неотрицательное число: '))
while n < 0:
    print('Введены неверные данные')
    n = int(input('Введите целое неотрицательное число: '))

def factorial_number(number):
    factorial = 1
    while  number>1:
        factorial*= number
        number-=1
    # for i in range(1,n+1):
    #     factorial*= i
    return factorial

factorial_n = factorial_number(n)
print(factorial_n)