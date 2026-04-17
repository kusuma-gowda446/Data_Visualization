import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [1, 2, 3])
plt.title("Graph 1")

plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [3, 2, 1])
plt.title("Graph 2")

plt.show()
