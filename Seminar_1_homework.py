# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# Решение задачи 6 

# num = int(input('Type any number in range from 1 to 7 -  '))
# if num == 6 or num == 7:
#     print('Yes, it is a weekend')
# else:
#     print('No, It is not a weekend')


# 7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Решение задачи 7

# for x in [0,1]:
#     for y in [0,1]:
#         for z in [0,1]:
#             a = not(x or y or z)
#             b = not x and not y and not z
#             f = a == b
#             print(x, y, z, f)



# 8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

# Решение задачи 8

# x = int(input('Type any number exept 0 for X =  '))
# y = int(input('Type any number exept 0 for Y =  '))
# if x == 0 and y == 0 or x == 0 or y == 0:
#     print('X and Y must not be 0. Please, enter any number other than zero')
# elif x > 0 and y > 0:
#     print('X =',x, 'Y =',y,'The point is located in quarter 1')
# elif x < 0 and y > 0:
#     print('X =',x, 'Y =',y,'The point is located in quarter 2')   
# elif x < 0 and y < 0:
#     print('X =',x, 'Y =',y,'The point is located in quarter 3')  
# elif x > 0 and y < 0:
#     print('X =',x, 'Y =',y,'The point is located in quarter 4')  

# 9. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Решение задачи 9

# quarter = int(input('Type number of quarter from 1 to 4 =  '))
# if quarter == 0 or quarter > 4 or quarter < 1:
#     print('Wrong nimber. Please, enter number from 1 to 4')
# elif quarter == 1:
#     print('The range of possible coordinates of points in this quarter', quarter,'is x > 0 and y > 0')
# elif quarter == 2:
#      print('The range of possible coordinates of points in this quarter', quarter,'is x < 0 and y > 0')
# elif quarter == 3:
#      print('The range of possible coordinates of points in this quarter', quarter,'is x < 0 and y < 0')
# elif quarter == 4:
#      print('The range of possible coordinates of points in this quarter', quarter,'is x > 0 and y < 0')

# 10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# Решение задачи 10 

# from math import sqrt
# x1 = int(input('Type number for x1 =  '))
# x2 = int(input('Type number for x2 =  '))
# y1 = int(input('Type number for y1 =  '))
# y2 = int(input('Type number for y2 =  '))
# print('point A (',x1,';',y1,')')
# print('point B (',x2,';',y2,')')
# distance_between_A_and_B = sqrt((x1 - x2)**2 + (y2 - y1)**2)
# print('Distance between point A and B is', round(distance_between_A_and_B, 2))