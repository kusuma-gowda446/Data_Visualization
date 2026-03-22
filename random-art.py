import matplotlib.pyplot as plt
import numpy as np

for i in range(100):
    x = np.random.rand(2)
    y = np.random.rand(2)
    plt.plot(x, y)

plt.title("Random Art")
plt.axis('off')
plt.show()
