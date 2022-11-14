from fractions import Fraction
x_1 = 0
y_1 = 0

x_2 = 0
y_2 = 0

def init_1(numerator, denominator):
    global x_1
    global y_1
    x_1 = numerator
    y_1 = denominator

def init_2(numerator, denominator):
    global x_2
    global y_2
    x_2 = numerator
    y_2 = denominator

def addition():
    return Fraction(x_1, y_1) + Fraction(x_2, y_2)    

def division():
    return Fraction(x_1, y_1) / Fraction(x_2, y_2) 

def multiplication():
    return Fraction(x_1, y_1) * Fraction(x_2, y_2)

def subtraction():
    return Fraction(x_1, y_1) - Fraction(x_2, y_2) 