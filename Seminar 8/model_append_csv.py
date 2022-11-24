import csv
import choice_of_action

def append_user():
    with open('Database.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        max_id = 1
        for row in reader:
            if max_id < int(row['id']):
               max_id = int(row['id'])
    with open('Database.csv', 'a', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name', 'number']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writerow({'id': max_id+1, 'second_name': choice_of_action.choice_of_data_add_second_name(),
                     'first_name': choice_of_action.choice_of_data_add_first_name(),
                     'last_name': choice_of_action.choice_of_data_add_last_name()})
    

