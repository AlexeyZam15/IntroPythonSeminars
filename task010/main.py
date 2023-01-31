# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint

n = int(input('Введите количество монет: '))

coins_side1 = []
for i in range(n):
    coins_side1.append(randint(0, 1))
print(f'Стороны монет, 0 - решка, 1 - герб:\n{coins_side1}')


def coins_sides(coins_side=[]):
    tails = 0
    eagles = 0
    for i in coins_side:
        if i == 0:
            tails += 1
        else:
            eagles += 1
    return tails, eagles


def coins_conditions_all_one_side(coins_side=[]):
    tails, eagles = coins_sides(coins_side)
    if tails == 0 or eagles == 0:
        print(f'Все монеты уже лежат на одной стороне')
    elif tails < eagles:
        print(f'Нужно перевернуть c решек: {tails}')
    else:
        print(f'Нужно перевернуть c гербов: {eagles}')


coins_conditions_all_one_side(coins_side1)
