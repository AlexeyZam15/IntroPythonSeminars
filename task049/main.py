# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# from math import pi
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#
#
# def max_square_orbits(list1):
#     res = []
#     max1 = pi * list1[0][0] * list1[0][1]
#     max1_a_b = (list1[0][0], list1[0][1])
#     for i in list1:
#         if pi * i[0] * i[1] > max1 and i[0] != i[1]:
#             max1 = pi * i[0] * i[1]
#             max1_a_b = (i[0], i[1])
#     return max1_a_b

# print(max_square_orbits(orbits))

from math import pi

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# orbits = [i for i in orbits if i[0] != i[1]]
orbits = list(filter(lambda i: i[0] != i[1], orbits))
# max_square = max([pi * i[0] * i[1] for i in orbits])
max_square = max(list(map(lambda x: pi * x[0] * x[1], orbits)))
# max_square_a_b = [i for i in orbits if pi * i[0] * i[1] == max_square]
max_square_a_b = list(filter(lambda y: pi * y[0] * y[1] == max_square, orbits))
print(*max_square_a_b)
