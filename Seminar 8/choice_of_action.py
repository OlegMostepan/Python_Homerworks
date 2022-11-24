def choice_of_action():
   while True:
        num = (input("Please choice action and input number: 1 for Write, 2 for Add , 3 for Change, 4 for Delete  ---  "))
        if num == '1' or num == '2' or num == '3' or num == '4':
            num = int(num)
            break
        else:
            print("Wrong number. Please choise 1 or 2 or 3 or 4 for actions")      
   return num
############# CHOICE TO ADD NEW DATA ##################        
def choice_of_data_add_second_name():
   while True:
    num = input("Please choice data to add: second_name ---  ")
    if num.isspace() or num.isalnum():
        break
    else:
        print("Wrong symbol. Please type letters")      
    return num

def choice_of_data_add_first_name():
   while True:
    num = input("Please choice data to add: first_name ---  ")
    if num.isspace() or num.isalnum():
        break
    else:
        print("Wrong symbol. Please type letters") 
    return num

def choice_of_data_add_last_name():
   while True:
    num = input("Please choice data to add: last_name ---  ")
    if num.isspace() or num.isalnum():
        break
    else:
        print("Wrong symbol. Please type letters")
    return num

################# CHANGES Of DATA by ID ##################################################
def change_of_data_choice_Id():
#    while True:
    return int(input("Please choice Id to make changes: Id ---  "))
    # if num.numerator():
    #     break
    # else:
    #     print("Wrong symbol. Please type letters")      
     
def change_of_data_second_name():
   while True:
    num = input("Please choice data to change: second_name ---  ")
    if num.isspace() or num.isalnum():
        break
    else:
        print("Wrong symbol. Please type letters")      
    return num

def change_of_data_first_name():
   while True:
    num = input("Please choice data to change: first_name ---  ")
    if num.isspace() or num.isalnum():
        break
    else:
        print("Wrong symbol. Please type letters") 
    return num

def change_of_data_last_name():
   while True:
    num = input("Please choice data to change: last_name ---  ")
    if num.isspace() or num.isalnum():
        break
    else:
        print("Wrong symbol. Please type letters")      
    return num