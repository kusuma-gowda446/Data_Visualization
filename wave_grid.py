import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

for i in range(5):
    y = np.sin(x + i)
    plt.plot(x, y)

plt.title("Wave Grid")
plt.show()
