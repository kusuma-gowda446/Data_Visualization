import matplotlib.pyplot as plt

for i in range(1, 10):
    plt.plot([i, i, -i, -i, i],
             [i, -i, -i, i, i])

plt.title("Concentric Squares")
plt.gca().set_aspect('equal')
plt.show()
