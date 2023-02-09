# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень k: '))
while k < 1:
    print('Введеные неверные данные')
    k = int(input('Введите натуральную степень k: '))

def create_random_polynom(x_max_degree):
    degrees = []
    for i in range(1, x_max_degree+1):
        degrees.append(i)

    coeffs = []
    for i in range(x_max_degree):
        coeffs.append(randint(0, 10))

    # expression = 0
    expression_string = ''
    c = randint(0, 10)

    for i in range(x_max_degree):
        if coeffs[i] > 0:
            expression_string += f'{coeffs[i]}*x^{degrees[i]} + '
        # expression += coeffs[i]*x**degrees[i]

    if expression_string != '':
        if c != 0:
            expression_string += f'{c}'
        else:
            expression_string = expression_string[:-3]
        expression_string += ' = 0'
        # print(expression_string)
    else:
        expression_string = 'Все коэффиценты многочлена равны 0'
    # expression += c
    return expression_string
 
expression_string1 = create_random_polynom(k)
with open('file.txt', 'w') as data:
    data.write(expression_string1)