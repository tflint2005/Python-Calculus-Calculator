from sympy import symbols, diff, sympify
import sympy as sp
from sympy import *

option = input(("What Caluclus 1 Topic do you need solved? \n 1. Derivative \n 2. Integral \n 3. Numerical Limit Approximation \n 4. Differentiate to Find Tangent line "))

x = symbols('x')
if option == '1':
    try:
        function = input("Enter a derivative (Example 3*x**2 = 3x^2): ")
        # Convert the string to a SymPy expression
        function = sympify(function)

        # the exception block just stops the program from crashing and gives an error message instead.
        result = diff(function, x)
        print(result)
    except Exception as e:
        print("An error has occured ")

if option == ('2'):
    try:
        integral = sympify(input("Integral calculator enter function here: "))
        start_interval = float(input("Enter the start of your interval: "))
        end_interval = float(input("Enter the end of your interval: "))

        result = integrate(integral, (x, start_interval, end_interval))
        print(result)
    except Exception as e:
        print("An error has occured ")

if option == ('3'):
    try:
        function_input = input("Limit calculator enter function here: ")
        x_value = float(input("Enter x value being approached: "))
        function = sympify(function_input)

        x = symbols('x')
        right1 = function.subs(x,x_value + 0.3)
        right2 = function.subs(x,x_value + 0.1)
        right3 = function.subs(x,x_value + 0.001)
        subx = function.subs(x, x_value)
        print(f"When approaching {x_value} from the right the graph approaches: {right1}, {right2}, {right3}")

        left1 = function.subs(x, x_value - 0.3)
        left2 = function.subs(x, x_value - 0.1)
        left3 = function.subs(x, x_value - 0.001)
        print(f"When approaching {x_value} from the right the graph approaches: {left1}, {left2}, {left3}") 
        print(f"The graph is approaching somewhere between {left3} and {right3} ") 
    except Exception as e:
        print("An error has occured ")

if option == ('4'):
    try:
        function = sp.sympify(input("Enter the function: "))

        x_value = float(input("Enter the x value "))
        x = sp.symbols('x')
        derivative = sp.diff(function, x)
        print(f"The derivative of the function is: {derivative} ")

        slope = round(derivative.subs(x, x_value).evalf())
        print(f"The slope when x = {x_value} is: {slope}")

        y_value = round(function.subs(x, x_value).evalf())
        print(f"The y-value of the original function when x = {x_value} is:{y_value} ")

#y-y1=M(x-x1)
        print(f"The tangent line of the given function is: y-{y_value}={slope}(x-{x_value}) ")
    except Exception as e:
        print("An error has occured ")