import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 2, 3])

plt.gca().invert_yaxis()

plt.title("Inverted Axis")
plt.show()
