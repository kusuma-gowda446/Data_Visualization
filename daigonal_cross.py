import matplotlib.pyplot as plt

for i in range(10):
    plt.plot([0, 10], [i, 10-i])
    plt.plot([0, 10], [10-i, i])

plt.title("Diagonal Cross Pattern")
plt.show()
