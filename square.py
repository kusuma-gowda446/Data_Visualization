import matplotlib.pyplot as plt

x = [0, 1, 1, 0, 0]
y = [0, 0, 1, 1, 0]

plt.plot(x, y)

plt.title("Square Pattern")
plt.gca().set_aspect('equal')
plt.show()
