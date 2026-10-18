# The following function computes the gradient of a two-term multivariable function.

import sympy as sp

def gradient(function_str):
    # Define variables
    x, y = sp.symbols('x y')

    # Convert the input string into a SymPy expression
    f = sp.sympify(function_str)

    # Compute partial derivatives
    df_dx = sp.diff(f, x)
    df_dy = sp.diff(f, y)

    # Print the result
    print(f"The gradient vector of the function f = {f} is \u2207f = ({df_dx}, {df_dy}).")

# Example usage
user_input = input("Enter a function of x and y: ")
gradient(user_input)