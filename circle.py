import matplotlib.pyplot as plt

circle = plt.Circle((0, 0), 1)

plt.gca().add_patch(circle)
plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.title("Simple Circle")
plt.gca().set_aspect('equal')
plt.show()
