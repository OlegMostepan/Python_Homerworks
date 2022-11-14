def get_numbers_numerator_1():
    return int(input("The 1st fraction number. Please input numerator 1 - "))
    
def get_numbers_denominator_1():
    while True:
        num = int(input("The 1st fraction number. Please input denominator 1 - "))
        if num !=0:
            break
        if num == 0:
            print("Division by zero. Choose a number other than zero") 
    return num

def get_numbers_numerator_2():
    return int(input("The 2nd fraction number. Please input numerator 2 - "))
    
def get_numbers_denominator_2():
    while True:
        num = int(input("The 2nd fraction number. Please input denominator 2 - "))
        if num !=0:
            break
        if num == 0:
            print("Division by zero. Choose a number other than zero") 
    return num

def print_result(data, title):
    print(f'{title} = {data}')

 