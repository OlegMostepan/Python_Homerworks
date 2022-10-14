# Урок 2. Знакомство с Python. Продолжение

# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Решение задачи 14 

# num = input('Введите любое число  ')
# if '.' or ',' in num:
#     num = num.replace('.', '')
#     num = num.replace(',', '')
#     print(sum(map(int, list(num))))
# else:
#     print(sum(map(int, list(num))))
 
# Комментарии к решению задачи 14  
# list(input()) --> разбить введенное на цифры
# map(int, list(input())) --> каждую цифру привести к целому (у нас ведь изначально текст)
# s(map(int, list(input()))) --> посчитать сумму цифр
# print(sum(map(int, list())))  --> вывести сумму



# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Решение задачи 15

# num = int (input('Введите любое число  '))
# print('Набор произведений чисел равен ')
# y = 1
# a = 1
# for x in range(1,num+1):
#     y = x * 1
#     a = a * y
#     print((a), end=" " )


# 16. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

# Решение задачи 16

# from operator import index

# num = int (input('Введите целое, положительное число  '))
# print('Последовательность чисел (1+1/n)^n равна')
# z=0
# for x in range(1,num+1):
#     y = (round(((1+(1/x))**x), 2))
#     z += y
#     print('{',index(x),':',y,'}', end=" " )
# print('Сумма чисел равна = ',z)


# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на введенных пользователем позициях.

# Решение задачи 17

# from operator import index

# num_positive = int (input('Введите целое, положительное число  '))
# tnum_negaive = int (input('Введите целое, отрицательное число  '))

# while num_positive < 0:
#     ValueError 
#     print('Ошибка, введите положительное число')
#     num_positive = int (input('Введите целое, положительное число  '))
   
# while tnum_negaive > 0:
#     ValueError 
#     print('Ошибка, введите отрицательное число')
#     tnum_negaive = int (input('Введите целое, отрицательное число  '))

# print('Последовательность чисел {индекс : число} в диапазоне от',tnum_negaive,'до',num_positive)
# for x in range(tnum_negaive,num_positive+1):
#     print('{',index(x),':',x,'}', end=" " )
# print()

# index_positive = int (input('Введите индекс, положительного числа  '))
# index_negaive = int (input('Введите индекс, отрицательного числа  '))

# while index_positive < 0:
#     ValueError 
#     print('Ошибка, введите индекс положительного числа')
#     index_positive = int (input('Введите индекс, положительного числа  '))

# while index_negaive> 0:
#     ValueError 
#     print('Ошибка, введите индекс отрицательного числа')
#     index_negaive = int (input('Введите индекс, отрицательного числа  '))

# for a in range(tnum_negaive, num_positive):
#     a = index(index_positive)
# for b in range(tnum_negaive, num_positive):
#     b = index(tnum_negaive)
# result = a * b 
# print('Произведение чисел', a,'умножить на', b,'=',result)

# 18. *Реализуйте алгоритм перемешивания списка.

# Решение задачи 18

# from operator import index
# import random

# num_positive = int (input('Введите целое, положительное число  '))
# num_negative = int (input('Введите целое, отрицательное число  '))
# print('Последовательность чисел {индекс : число} в диапазоне от',num_negative,'до',num_positive)

# my_list = list(range(num_negative, num_positive+1))
    
# print(my_list,' Исходный список', end='')
# print()    
# random.shuffle(my_list)
# print(my_list,' Перемешанный список', end='')   
