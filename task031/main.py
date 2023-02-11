# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak= ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def Fibonacci(n: int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input('Введите номер числа Фибоначчи: '))
for i in range(1,n+1):
    num_fib = Fibonacci(i)
    print(i, '-', num_fib)

print(n, 'число Фибоначчи - ', Fibonacci(n))