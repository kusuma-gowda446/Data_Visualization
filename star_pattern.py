import matplotlib.pyplot as plt

for i in range(20):
    plt.plot([0, i], [0, 20-i])

plt.title("Star Pattern")
plt.show()
