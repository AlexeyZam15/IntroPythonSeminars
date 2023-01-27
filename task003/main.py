# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# class1 = int(input("Введите кол-во учащихся для первого класса: "))
# class2 = int(input("Введите кол-во учащихся для второго класса: "))
# class3 = int(input("Введите кол-во учащихся для третьего класса: "))

# res = (class1+class2+class3+1)//2
# print(f"Потребуется приобрести {res} парт")

number_classes1 = int(input("Введите кол-во новых классов: "))
classes_pupils1 = []

for i in range(number_classes1):
    classes_pupils1.append(int(input(f"Введите учеников в новом классе № {i}: ")))
    
def DesksCalculation(classes_pupils = []):
    sum = 0
    for i in range(len(classes_pupils)):
        sum += classes_pupils[i]
    desks = (sum + 2 - 1)//2
    return desks

desks1 = DesksCalculation(classes_pupils1)
print(f"Потребуется приобрести парт: {desks1}")