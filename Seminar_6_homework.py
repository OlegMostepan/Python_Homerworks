
# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Решение задачи 2

# import math

# a = [2, 3, 5, 6, 7]

# for i in range(math.ceil(len(a)/2)):  # вариант 1 
#         c = a[i] * a[len(a)-i-1] 
#         print(a[i],'*',a[len(a)-i-1],'=',c)
    
# ################  Решение задачи с LIST COMPREHENSION ###################

# a = [a[i] * a[len(a)-i-1] for i in range(math.ceil(len(a)/2)) ]
# print (a)




















# Урок 4. Данные, функции и модули в Python. Продолжение

# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt. 
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи

# Решение задачи 30

# file = open('users.txt', encoding='utf-8')
# onstring = file.read()
# file.close

# file1 = open('hobby.txt', encoding='utf-8')
# onstring1 = file1.read()
# file.close

# d ={}                     
# for text in onstring :        
#     key = onstring.split('\n')
# for text1 in onstring1:  
#     values = onstring1.split('\n') 
#     d = dict(zip(key, values))
              
# print(d)

# file2 = open('users_hobby.txt','w', encoding='utf-8') 
# file2.write(str(d))
# file2.close


# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Решение задачи 31

# import math

# n = int(input("Введите число "))
# while n % 2 == 0:
#         print (2)
#         n = n / 2
# for i in range(3,int(math.sqrt(n))+1,2):
#         while n % i== 0:
#             print (i)
#             n = n / i
# if n > 2:
#     print (n)



# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Решение задачи 32

# from typing import Counter

# n = [1, 2, 2, 3, 3, 4,4,6,7, 5]
# c = Counter(n)
# print(c, 'Элементы отображаются в порядке возрастания и не соответствуют порядку расположения в исходном списке, в начале идут повторяющиеся элементы, а затем не повторяющиеся. Key - это значение элемента как в исходном списке. Value - это кол-во повторений элемента.')
# print(dict(c), 'Элементы отображаются в порядке расположения как в исходном списке. Key - это значение элемента как в исходном списке. Value - это кол-во повторений элемента.')
# for  key, value in c.items():
#     if value == 1:
#         print (key, end = ", ")
# print(' - не повторяющиеся элементы списка')


# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0


# from random import randrange


# k = randrange(1,4)
# a = [randrange(1,100) for i in range(k)]
# polynominal = '+'.join([f'{j}x^{i}' for i, j in enumerate(a) if j][::-1])
# print(polynominal)
# #Записываем многочлен в Polynominal.txt
# file = open('Polynominal.txt','w', encoding='utf-8') 
# file.write(polynominal)
# file.close

# 34. *Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0

# from operator import index
# from random import randrange
# from select import select
# import re


# # СОЗДАЕМ 1_POLYNOMINAL

# k = 2 #randrange(0,8)
# a = [randrange(0,100) for i in range(k)]
# polynominal_1 = '+'.join([f'{j}x^{i}' for i, j in enumerate(a) if j][::-1])
# print('Polinominal_1 = ', polynominal_1)

# Записываем многочлен в 1_Polynominal.txt
# file = open('1_Polynominal.txt','w', encoding='utf-8') 
# file.write(polynominal_1)
# file.close

# # СОЗДАЕМ 2_POLYNOMINAL

# k = 2 #randrange(0,8)
# a = [randrange(0,100) for i in range(k)]
# polynominal_2 = '+'.join([f'{j}x^{i}' for i, j in enumerate(a) if j][::-1])

# print('Polinominal_2 = ', polynominal_2)

# # Записываем многочлен в 2_Polynominal.txt
# file = open('1_Polynominal.txt','w', encoding='utf-8') 
# file.write(polynominal_2)
# file.close

# # # СУММИРУЕМ 1_POLYNOMINAL + 2_POLYNOMINAL  = Sun_Polynominal


# print(re.findall(r'\w+\d+', polynominal_1)) # там и не смог добиться чтобы однозначный коэффициент при Х считывался. Считывает только двузначные. 
# print(re.findall(r'\w+\d+', polynominal_2))

