import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.figure(figsize=(8,5))
plt.plot(x, y, marker='o', linestyle='--')
plt.title("Simple Trend Line")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid()

plt.show()
