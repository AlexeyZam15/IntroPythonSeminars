# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

string = input("Введите строку: ")

set1 = set(string.split(' '))
# print(set1)

string = string.replace(' ', '')

dict1 = dict()

for i in set1:
    dict1[i] = 0
# print(dict1)

for i in string:
    if dict1[i] == 0:
        print(i,end=' ')
    else:
        print(f'{i}_{dict1[i]}',end=' ')
    dict1[i] +=1
