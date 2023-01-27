# Задача 8: Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

rows_chocolate = int(input("Введите кол-во рядов в шоколадке: "))
columns_chocolate = int(input("Введите кол-во столбцов в шоколадке: "))
broken_pieces = int(input("Введите кол-во долек, которое хотите отломать: "))

if ((broken_pieces % rows_chocolate == 0 or broken_pieces % columns_chocolate == 0)
        and broken_pieces < rows_chocolate*columns_chocolate):
    print("Шоколадку можно разломить на два прямоугольника")
else:
    print("Шоколадку нельзя разломить на два прямоугольника")
