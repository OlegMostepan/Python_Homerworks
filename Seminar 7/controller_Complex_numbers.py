import model_complex_numbers_Addition as model_ADD
import model_complex_numbers_Division as model_DIV
import model_complex_numbers_Muitiplication as model_MULTP
import model_complex_numbers_Subtraction as model_SUBTR
import view_Complex
import choice_of_calculation

def start_calc_Complex():
    Action = (choice_of_calculation.choice_of_calc())
    Fist_number_real = (view_Complex.get_numbers_real_1())
    Fist_number_imag = (view_Complex.get_numbers_imag_1())
    Second_munber_real = (view_Complex.get_numbers_real_2())
    Second_munber_imag = (view_Complex.get_numbers_imag_2())
    if Action == 1:
        model_ADD.init_1(Fist_number_real, Fist_number_imag)
        model_ADD.init_2(Second_munber_real, Second_munber_imag)
        result = model_ADD.addition()
        view_Complex.print_result(result, "Result of addition " )
    if Action == 4:
        model_DIV.init_1(Fist_number_real, Fist_number_imag)
        model_DIV.init_2(Second_munber_real, Second_munber_imag)
        result = model_DIV.division()
        view_Complex.print_result(result, "Result of division " )
    if Action == 3:
        model_MULTP.init_1(Fist_number_real, Fist_number_imag)
        model_MULTP.init_2(Second_munber_real, Second_munber_imag)
        result = model_MULTP.multiplication()
        view_Complex.print_result(result, "Result of multiplication " )
    if Action == 2:
        model_SUBTR.init_1(Fist_number_real, Fist_number_imag)
        model_SUBTR.init_2(Second_munber_real, Second_munber_imag)
        result = model_SUBTR.subtraction()
        view_Complex.print_result(result, "Result of subtraction " )        






    
     