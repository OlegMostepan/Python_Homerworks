import csv
def write_header():
    with open('Database.csv', 'w', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'first_name', 'second_name', 'last_name']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csv_writer.writeheader()
        for i in range(1, 11):
            csv_writer.writerow(
                {'id': i, 'second_name': f"отчество_{i}",
                'first_name': f"имя_{i}", 'last_name': f"фамилия_{i}"}
            )
    return write_header