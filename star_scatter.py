import matplotlib.pyplot as plt
import random

x = [random.randint(1, 100) for _ in range(100)]
y = [random.randint(1, 100) for _ in range(100)]

plt.scatter(x, y, marker="*", s=100)

plt.title("Star Pattern")

plt.show()
