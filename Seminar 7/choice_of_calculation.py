def choice_of_calc():
   while True:
        num = (input("Please choice math operation and input number: 1 for +, 2 for -, 3 for *, 4 for /  ---  "))
        if num == '1' or num == '2' or num == '3' or num == '4':
            num = int(num)
            break
        else:
            print("Wrong simbol. Please choise 1 or 2 or 3 or 4 for math operation")      
   return num
        
    
    # num = (input("Please choice math operation and input number: 1 for +, 2 for -, 3 for *, 4 for /  ---  "))
    
    # num = (input("Please choice math operation and input number: 1 for +, 2 for -, 3 for *, 4 for /  ---  "))
    # if num.isdigit(): 
    #         num = int(num)
    # else:
    #     return print("Wrong simbol. Please choise 1 or 2 or 3 or 4 for math operation")  
                
    # return int(num)             
            
#             # if num == "1" or num == "2" or num == "3" or num == "4":
#             #     return num
#             # else:
#             #     print("Wrong simbol. Please choise 1 or 2 or 3 o4 for math operation")  

# # def check_user_input(input):
# #     try:
#         val != int(input)
#         print("Wrong simbol. Please choise 1 or 2 or 3 o4 for math operation")  
#     except ValueError: