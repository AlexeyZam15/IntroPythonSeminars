# извлечение элементов множества из словаря

dictionary = {}

potionA, potionB, potionC = 'зельеА', 'зельеБ', 'зельеЦ'


dictionary['half-blood'] = 'полукровка'
dictionary['cauldron'] = 'котёл'
dictionary['potion'] = {'зельеА', 'зельеБ', 'зельеЦ'}

# def print_dict_values(dictionary1: dict):
#     for i in dictionary1:
#         try:
#             if type(dictionary1[i]) == set:
#                 print_dict_values(dictionary1[i])
#             else:
#                 print(dictionary1[i])
#         except TypeError:
#             print(i)

# print_dict_values(dictionary)

for i in dictionary:
    if type(dictionary[i]) == set:
        for j in dictionary[i]:
            print(j)
    else:
        print(dictionary[i])