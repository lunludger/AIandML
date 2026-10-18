# The program applies the power rule to a polynomial with one term. 
# The program prompts the user to enter
# - the coefficient
# - the power of a polynomial term and 
# - the x-coordinate of the point where the user 
#   would like to calculate the gradient

coefficient = int(input(" Enter the coefficient of x: "))
power = int(input(" Enter the power to raise x: "))
x = int(input("Enter x-coordinate of the point where the user \n"
              "would like to calculate the gradient: "))

# Apply the power rule to find the derivative
updated_coefficient = coefficient * power
updated_power = power - 1

# Calculate the gradient m at the given x-coordinate
gradient = updated_coefficient * (x ** updated_power)

# Expected output
print(f"The derivative of the polynomial {coefficient}X^{power} is {updated_coefficient}X^{updated_power}")
print(f"The gradient at the point x = {x} is {gradient}")

