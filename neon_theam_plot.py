import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")

x = np.arange(1, 11)
y = x**2

plt.plot(x, y, color='cyan', linewidth=3, marker='o')
plt.title("Neon Plot", color='lime')
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
