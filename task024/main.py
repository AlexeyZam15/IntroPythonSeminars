# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

from random import randint


def sum_closest_list_elements(list1: list, element_index: int, number_closest_elements: int):
    sum_closest_elements = 0
    size_list1 = len(list1)
    element_index = element_index-number_closest_elements//2
    number_iterations = number_closest_elements+1
    while number_iterations > size_list1:
        number_iterations-=1
    for i in range(number_iterations):
        # print(element_index, list1[element_index])
        sum_closest_elements += list1[element_index]
        element_index += 1
        if element_index > size_list1 - 1:
            element_index = 0
    return sum_closest_elements

number_bushes = int(input('Введите кол-во кустов: '))
bushes_berries = [randint(1, 10) for i in range(number_bushes)]
print('Ягод на кустах:\n',*bushes_berries)

bush_number = int(input('Введите номер куста: '))
while number_bushes < bush_number or bush_number <= 0:
    print(f'Введены неверные данные. Всего кустов: {number_bushes}')
    print('Ягод на кустах:\n',*bushes_berries)
    bush_number = int(input('Введите номер куста: '))

print(sum_closest_list_elements(bushes_berries, bush_number-1, 2))
