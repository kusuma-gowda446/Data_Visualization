import matplotlib.pyplot as plt

for i in range(0, 11):
    plt.plot([0, 10], [i, i])   # horizontal lines
    plt.plot([i, i], [0, 10])   # vertical lines

plt.title("Grid Pattern")
plt.gca().set_aspect('equal')
plt.show()
