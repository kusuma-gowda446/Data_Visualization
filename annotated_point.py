import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 5, 3]

plt.plot(x, y)

plt.annotate("Max", (2, 5))

plt.title("Annotation")
plt.show()
