import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.arange(1, 11)
y1 = x
y2 = x**2
y3 = x**3

# Create figure
plt.figure(figsize=(10,6))

# Plot different lines
plt.plot(x, y1, marker='o', linewidth=2, label="Linear")
plt.plot(x, y2, marker='s', linewidth=2, label="Square")
plt.plot(x, y3, marker='^', linewidth=2, label="Cube")

# Labels and title
plt.title("Comparison of Different Functions")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Grid and legend
plt.grid(True)
plt.legend()

# Show plot
plt.show()
