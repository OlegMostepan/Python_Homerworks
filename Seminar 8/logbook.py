from datetime import datetime

def logs(data, title):
    time = datetime.now().strftime('%H:%M_%D')
    with open('logbook.txt', 'a', encoding= 'utf-8') as file:
        file.write(('{}; Action done ;{};{}\n').format(time, data, title))

