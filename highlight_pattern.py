import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x, y)

# Highlight max value
max_y = max(y)
max_x = x[y.index(max_y)]

plt.scatter(max_x, max_y)
plt.text(max_x, max_y, " Peak")

plt.title("Highlight Pattern")
plt.show()
