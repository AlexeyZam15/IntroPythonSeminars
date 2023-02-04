# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dict1 = \
#     {"V": "S001", "V": "S002", "VI": "S001",
#      "VI": "S005", "VII": " S005 ", " V ": " S009 ", " VIII": " S007 "}

# print(dict1)

# print(set(dict1.values()))

# print(dict1)

# set1 = set()
# for i in dict1:
#     for key in i.keys():
#         set1.add(i[key])

# print(set1)

dict1 = \
    [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
     {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}]

print(dict1)

set1 = set()
for i in dict1:
    for value in i.values():
        set1.add(value.strip())

print(set1)
