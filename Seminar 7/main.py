import controller_Complex_numbers
import controller_Fraction_numbers



num = int(input("Please choice type of numbers for math operation and input number: 1 for Complex numbers, 2 for Fraction ---  "))
if num == 1:
    controller_Complex_numbers.start_calc_Complex()
if num == 2:
    controller_Fraction_numbers.start_calc_Fraction()