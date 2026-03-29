import matplotlib.pyplot as plt
import numpy as np

for i in range(50):
    circle = plt.Circle((np.random.rand()*10, np.random.rand()*10),
                        np.random.rand(),
                        fill=False)
    plt.gca().add_patch(circle)

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.title("Random Circles Art")
plt.gca().set_aspect('equal')
plt.show()
