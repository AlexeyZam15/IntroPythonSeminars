# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = input('Введите точность: ')
set1 = set(d).union({'0','1','.'})
while len(set1)>3:
    print('Введены неверные данные.')
    d = input('Введите точность: ')
    set1 = set(d)

d = d.replace('.','')

pi = math.pi
print(format(pi,f'0.{len(d)}'))
