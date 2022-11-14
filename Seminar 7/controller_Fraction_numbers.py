import model_Fraction_numbers_Addition_Division_Muitp_Subtr as model_Fraction
import view_Fraction
import choice_of_calculation

def start_calc_Fraction():
    Action = (choice_of_calculation.choice_of_calc())
    Fist_number_numerator = (view_Fraction.get_numbers_numerator_1())
    Fist_number_denominator = (view_Fraction.get_numbers_denominator_1())
    Second_munber_numerator = (view_Fraction.get_numbers_numerator_2())
    Second_munber_denominator = (view_Fraction.get_numbers_denominator_2())
    if Action == 1:
        model_Fraction.init_1(Fist_number_numerator, Fist_number_denominator)
        model_Fraction.init_2(Second_munber_numerator, Second_munber_denominator)
        result = model_Fraction.addition()
        view_Fraction.print_result(result, "Result of addition " )
    if Action == 4:
        model_Fraction.init_1(Fist_number_numerator, Fist_number_denominator)
        model_Fraction.init_2(Second_munber_numerator, Second_munber_denominator)
        result = model_Fraction.division()
        view_Fraction.print_result(result, "Result of division " )
    if Action == 3:
        model_Fraction.init_1(Fist_number_numerator, Fist_number_denominator)
        model_Fraction.init_2(Second_munber_numerator, Second_munber_denominator)
        result = model_Fraction.multiplication()
        view_Fraction.print_result(result, "Result of multiplication " )
    if Action == 2:
        model_Fraction.init_1(Fist_number_numerator, Fist_number_denominator)
        model_Fraction.init_2(Second_munber_numerator, Second_munber_denominator)
        result = model_Fraction.subtraction()
        view_Fraction.print_result(result, "Result of subtraction " )        






    
     