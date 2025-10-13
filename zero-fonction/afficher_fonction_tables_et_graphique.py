import matplotlib.pyplot as plt
import numpy as np
from fonctions import f2 as f
from tabulate import tabulate

# Print a table of values
table = [[x, round(f(x), 2)] for x in range(33)]
print(tabulate(table))

x_values = np.linspace(0, 32, 400)
y_values = f(x_values)
plt.plot(x_values, y_values)

# Add labels and legend
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
