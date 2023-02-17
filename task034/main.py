# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам

def vowels_amount_equal(text0):
    vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
    # vowels_amount = []
    # for i in text0.split():
    #     counter = 0
    #     for j in i.split('-'):
    #         counter += len(list(filter(lambda x: x in vowels, j)))
    # #     counter = sum([len(list(filter(lambda x: x in vowels, j))) for j in i.split('-')])
    #     vowels_amount.append(counter)
    vowels_amount = list(
        map(lambda y: sum([len(list(filter(lambda x: x in vowels, j))) for j in y.split('-')]), text0.split()))
    return all([x == vowels_amount[0] for x in vowels_amount])


# 'пара-ра-рам рам-пам-папам па-ра-па-дам'
text = input('Введите стихотворение \n')

print('Ответ:', 'Парам пам-пам' if vowels_amount_equal(text) else 'Пам парам')