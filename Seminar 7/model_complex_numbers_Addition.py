
x_1 = 0
y_1 = 0

x_2 = 0
y_2 = 0

def init_1(real, imag):
    global x_1
    global y_1
    x_1 = real
    y_1 = imag

def init_2(real, imag):
    global x_2
    global y_2
    x_2 = real
    y_2 = imag

def addition():
    return complex(x_1, y_1) + complex(x_2, y_2)    


