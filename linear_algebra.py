import numpy as np
import matplotlib.pyplot as plt

# Create a sequence of numbers going from 0 to 100 in intervals of 0.5
start_val = 0
stop_val = 100
n_samples = 200
X = np.linspace(start_val, stop_val, n_samples)

params = np.array([2, -5])

"""
-----------------
Task 1
------------------

Plot f(x) = P.X, where p is your params
"""

# parameter of matrix
m = params[0]  # is the slope
c = params[1]  # is the intercept

# The linear function is in the form
Y = m * X + c

# Plotting the graph  which is the slope of a straight line
plt.plot(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("The graph of f(x) = 2x - 5" )
plt.show()

