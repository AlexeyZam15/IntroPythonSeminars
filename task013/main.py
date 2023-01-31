# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


import random

n = int(input('Введите количество дней: '))

list1 = []
count = [0]
for i in range(n):
    list1.append(random.randint(-50, 50))

print(f"Температура по дням, в цельсиях:\n {list1}")

index = 0

for i in range(len(list1)):
    if list1[i] > 0:
        if len(count)-1 < index:
            count.append(0)
        count[index] += 1
    else:
        if len(count) > index:
            if count[index] != 0:
                index += 1
print(f"Продолжительность оттепелей, в днях:\n {count}")

max = count[0]
for i in range(len(count)):
    if count[i] > max:
        max = count[i]
print(f"Самая длинная оттепель длилась дней: {max}")
