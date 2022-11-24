import csv
import choice_of_action

# def change_user():
#     with open('Database.csv', 'r', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         max_id = choice_of_action.change_of_data_choice_Id()
#         print(max_id)
#         for row in reader:
#             if max_id == row['id']:
#                int(row['id']) == max_id
#             print (row['id'])   
#     with open('Database_changed.csv', 'w', encoding='utf-8', newline='') as csvfile:
#         fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
#         csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         csv_writer.writerow({'id': max_id, 'second_name': choice_of_action.change_of_data_second_name(),
#                      'first_name': choice_of_action.change_of_data_first_name(),
#                      'last_name': choice_of_action.change_of_data_last_name()})
    
def change_user():
    input = open('Database.csv', 'r', encoding='utf-8')
    output = open('Database_changed.csv', 'w', encoding='utf-8', newline='')
    reader = csv.DictReader(input)
    fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    max_id = choice_of_action.change_of_data_choice_Id()
    for row in reader:
        if row['id'] == max_id:
            writer.writerow({'id': max_id, 'second_name': choice_of_action.change_of_data_second_name(),
                     'first_name': choice_of_action.change_of_data_first_name(),
                     'last_name': choice_of_action.change_of_data_last_name()})
    
