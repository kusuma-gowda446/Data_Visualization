import matplotlib.pyplot as plt

plt.plot([0, 5], [0, 5])
plt.plot([0, 5], [5, 0])

plt.title("X Pattern")
plt.gca().set_aspect('equal')
plt.show()
