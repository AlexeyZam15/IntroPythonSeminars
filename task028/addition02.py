# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


def win_candies_game(candies, max_candies_per_turn):
    return candies % (max_candies_per_turn + 1) if max_candies_per_turn < candies else candies


candies1 = int(input('Введите кол-во конфет: '))

max_candies1 = int(input('Введите максимальное кол-во конфет, которое можно взять за ход: '))

print('Игра начинается')
print('Всего конфет:', candies1)
print('Максимум можно взять за ход:', max_candies1 if candies1 > max_candies1 else candies1)

print('Кто ходит первым? игрок - 1, бот - 2')
first_turn = input()
while first_turn != '1' and first_turn != '2':
    print('Неправильный ввод')
    print('Кто ходит первым? игрок - 1, бот - 2')
    first_turn = input()

print('Ходите играть с глупым или умным ботом? 1 - глупый, 2 - умный')
bot_difficulty = input()
while bot_difficulty != '1' and bot_difficulty != '2':
    print('Неправильный ввод')
    print('Ходите играть с глупым или умным ботом? 1 - глупый, 2 - умный')
    bot_difficulty = input()

smart_bot = False

if bot_difficulty == '2':
    smart_bot = True

if first_turn == '1':
    players = ('player', 'bot')
else:
    players = ('bot', 'player')

turns = 0

player_turn = True

if first_turn == '2':
    player_turn = False

while candies1 > 0:
    if player_turn:
        print('Конфет осталось:', candies1)
        print('Конфет необходимо взять чтобы выиграть:', win_candies_game(candies1, max_candies1))
        take_candies = (int(input('Сколько конфет возьмёте?: ')))
        while take_candies > max_candies1 or take_candies < 1 or take_candies > candies1:
            print("Неправильный ввод.")
            print('Конфет осталось:', candies1)
            print('Максимум можно взять конфет:', max_candies1 if candies1 > max_candies1 else candies1)
            take_candies = (int(input('Сколько конфет возьмёте?: ')))
        player_turn = False
    else:
        print('Конфет осталось:', candies1)
        if smart_bot:
            take_candies = win_candies_game(candies1, max_candies1) if win_candies_game(candies1, max_candies1) > 0 \
                else randint(1, max_candies1) if candies1 > max_candies1 else randint(1, candies1)
        else:
            take_candies = randint(1, max_candies1) if candies1 > max_candies1 else randint(1, candies1)
        print('Противник берёт конфет:', take_candies)
        player_turn = True

    candies1 -= take_candies
    turns += 1

print('Игра закончилась')
print('Победил', players[1] if turns % 2 == 0 else players[0])
