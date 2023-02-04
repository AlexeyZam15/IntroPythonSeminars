# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def mult_couple_elements_list(l=list()):
    mult_list = list()
    for i in range((len(l)+1)//2):
        mult_list.append(l[i]*l[len(l)-i-1])
    return mult_list


list1 = [randint(0, 9) for i in range(int(input('Введите размер списка: ')))]
print(f'- {list1}', end=' => ')

mult_list1 = mult_couple_elements_list(list1)

print(mult_list1)
