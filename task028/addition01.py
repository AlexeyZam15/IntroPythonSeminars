# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('input.txt', 'w') as data:
    data.write(input())

text = ''

with open('input.txt', 'r') as data:
    for line in data:
        text += line

text_list = text.split()

for i in range(len(text_list) - 1, -1, -1):
    if "абв" in text_list[i]:
        text_list.remove(text_list[i])

text = ' '.join(text_list)

with open('output.txt', 'w', encoding='UTF-8') as data:
    data.write(text)

print(text)
