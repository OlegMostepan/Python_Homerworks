
# a = [number = '1',
# имя =  'Иван',
# отчество = 'Иванович',
# фамилия = 'Иванов',
# number = '2', 
# имя = 'Петр',
# отчество = 'Петрович',
# фамилия = 'Петров']


person_data = ['id', 'Иван','Иванович','Иванов']  #[number, имя , отчество, фамилия]


headers = ['id','first_name','second_name','last_name']
# a = len(person_data)
# print(a)
# b = len(headers)
# print(b)
# print (a/b)
# for i in range(1, 5):
dict_1 = { headers : person_data for (headers, person_data) in zip(headers, person_data) }
# for i in range(0, (int(len(person_data)/len(headers)))):
    # dict_1 = dict(zip(headers, person_data))
# print(dict_1)
# print(type(headers))
# print(type(person_data))

# dict1 = {id : 1, first_name :'имя', second_name : 'очество', last_name : 'фамилия'}

# 1,имя_1,отчество_1,фамилия_1