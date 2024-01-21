#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


def f1(x):
    return (x - 31) * (x + 2) * (x + 4)


def f2(x):
    return np.sin(np.pi * (x - 4) / 8) * (x - 16)


f = f1

# Print a table of values
table = [[x, round(f(x), 2)] for x in range(33)]
print(tabulate(table))

# Generate x values
x_values = np.linspace(0, 32, 400)
# Generate y values using the function
y_values = f(x_values)

# Plot the function
plt.plot(x_values, y_values)

# Add labels and legend
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
