# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))


def list_fibonacci(count: int):
    l = list()
    l.append(0)
    l.append(1)
    for i in range(2, count+1):
        l.append(l[i-2]+l[i-1])
    l1 = list()
    for i in range(1, count+1):
        l1.append(((-1)**(i-1))*l[i])
    l1.reverse()
    return l1 + l

print(list_fibonacci(k))
