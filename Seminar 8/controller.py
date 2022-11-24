import model_write_csv
import model_append_csv
import model_change_csv

import view
import choice_of_action
import logbook as log



def start_action():
    Action = choice_of_action.choice_of_action() 
    if Action == 1:
       result = model_write_csv.write_header()
       log.logs(result, 'Writed')
    if Action == 2:
       result = model_append_csv.append_user()
       log.logs(result, 'Added')
    if Action == 3:
       result = model_change_csv.change_user()
       log.logs(result, 'Changed')
    




    
     