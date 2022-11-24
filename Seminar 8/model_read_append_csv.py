# import csv



# with open('Database.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     max_id = 1
#     for row in reader:
#         if max_id < int(row['id']):
#             max_id = int(row['id'])
            

# with open('Database.csv', 'a', encoding='utf-8') as csvfile:
#     field_names = ['id', 'first_name', 'second_name', 'last_name']
#     csv_writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     csv_writer.writerow({'id': max_id+1, 'second_name': "Петрович",
#                      'first_name': "Петр",
#                      'last_name': "Петров"})
    

