# Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension

# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 201 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# import random

# list_of_players = ['player_1', 'player_2']
# player_1 = list_of_players[0] # игрок человек
# player_2 = list_of_players[1] # игрок человек
# min = 1  # минимальное количество конфет которое можно взять
# max = 28 # максимальное количество конфет которое можно взять
# x = 81  # общее количество конфет

# start_player = random.choice(list_of_players)
# print('Первым ходит',start_player)
# while x > 0:
#     print('Количество оставшихся конфет: {}'.format(x))
#     while True:
#             player_numb = int(input( 'Введите число конфет которые хотите забрать от {} до {} - {} -- '.format(min, max, start_player)))
#             if player_numb >= min and player_numb <= max:
#                 break
#     x = x - player_numb
#     start_player = player_1 if start_player == player_2 else player_2
# if start_player == player_2:
#     print('Победил player_1')
# else:
#     start_player == player_1
#     print('Победил player_2') 

 

# a) Добавьте игру против бота

# import random

# list_of_players = ['player_1', 'player_bot']
# player_1 = list_of_players[0]   # игрок человек
# player_bot = list_of_players[1] # заменил игрока на бота
# min = 1  # минимальное количество конфет которое можно взять
# max = 28 # максимальное количество конфет которое можно взять
# x = 81  # общее количество конфет
# start_player = random.choice(list_of_players)
# print('Первым ходит',start_player)
# while x > 0:
#     print('Количество оставшихся конфет: {}'.format(x))
#     while True:
#             if start_player == player_1:
#                 player_numb = int(input( 'Введите число конфет которые хотите забрать от {} до {} - {} -- '.format(min, max, player_1)))
#                 if player_numb >= min and player_numb <= max:
#                     break
#             elif start_player == player_bot:
#                 player_numb_bot = random.randint(min,max) # выбор числа для бота
#                 print('Введите число конфет которые хотите забрать от {} до {} - {} -- {}'.format(min, max, player_bot, player_numb_bot)) 
#                 player_numb = player_numb_bot
#                 if player_numb_bot >= min and player_numb_bot <= max:
#                     break
#     x = x - player_numb 
#     start_player = player_1 if start_player == player_bot else player_bot
# if start_player == player_bot:
#     print('Победил player_1')
# else:
#     start_player == player_1
#     print('Победил player_bot')   

# b) * Подумайте как наделить бота ""интеллектом""
# import random

# list_of_players = ['player_1', 'player_bot']
# player_1 = list_of_players[0]
# player_bot = list_of_players[1]
# min = 1 # минимальное количество конфет которое можно взять
# max = 5 # максимальное количество конфет которое можно взять
# x = 20  # общее количество конфет

# start_player = random.choice(list_of_players)
# print('Первым ходит',start_player)

# while x > 0:
#     print('Количество оставшихся конфет: {}'.format(x))
#     while True:
#             if start_player == player_1:
#                 player_numb = int(input('Введите число конфет которые хотите забрать от {} до {} - {} -- '.format(min, max, player_1)))
#                 if player_numb >= min and player_numb <= max:
#                     break
#             elif start_player == player_bot:
#                 i = x - (max+1)
#                 for i in range(min,max):   # условия выбора числа дают боту некоторый  "интеллект "
#                     player_numb_bot = i
#                     if x == max + 2:
#                         player_numb_bot = 1
#                     if x == max + 2 + max:
#                         player_numb_bot = max
#                     if x == max + 2:
#                         player_numb_bot = 1 
#                     if x == max:
#                         player_numb_bot = max      
#                 print('Введите число конфет которые хотите забрать от {} до {} - {} -- {}'.format(min, max, player_bot, player_numb_bot)) 
#                 player_numb = player_numb_bot
#                 if player_numb_bot >= min and player_numb_bot <= max:
#                     break
#     x = x - player_numb 
#     start_player = player_1 if start_player == player_bot else player_bot
# if start_player == player_bot:
#     print('Победил player_1')
# else:
#     start_player == player_1
#     print('Победил player_bot')   

# 2. Создайте программу для игры в ""Крестики-нолики"".
# board = list(range(1,10))

# def draw_board(board):
# print ("-" * 13)
# for x in range(3):
#         print ("|", board[0+x*3], "|", board[1+x*3], "|", board[2+x*3], "|")
#         print ("-" * 13)

# # def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(board)


# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

 
# file = open('RLE входные данные.txt', encoding='utf-8')
# text = file.read()
# file.close
# print(text)
# ###################################
# def encode(data):
#     encoding = ""
#     prev_char = ""
#     count = 1
    
#     for char in data:
#         if char != prev_char:
#             if prev_char:
#                 encoding += str(count) + prev_char
#             count = 1 
#             prev_char = char
#         else:
#             count += 1
#     else:
#         encoding += str(count) + prev_char
#         return encoding
# encode_text = encode(text)

# print(encode_text)
# ###################################
# def decode(data):
#     decode = ""
#     count = ''

#     for char in data:
#         if char.isdigit():
#          count += char
#         else:  
#          decode += char * int(count)
#          count = ''
#     return decode
# decode_text = decode(encode_text)

# print(decode_text)

# file1 = open('RLE выходные данные.txt','w', encoding='utf-8') 
# file1.write(decode_text)
# file1.close
