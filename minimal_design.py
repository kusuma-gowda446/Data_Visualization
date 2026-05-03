import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,20,25,30]

plt.figure(figsize=(8,5))
plt.plot(x, y)

# Remove top & right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.title("Minimal Design")
plt.show()
