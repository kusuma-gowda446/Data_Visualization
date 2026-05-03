import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(10,8))

axs[0,0].plot([1,2,3],[2,4,6])
axs[0,0].set_title("Line")

axs[0,1].bar(["A","B","C"], [5,7,6])
axs[0,1].set_title("Bar")

axs[1,0].scatter([1,2,3],[3,2,5])
axs[1,0].set_title("Scatter")

axs[1,1].pie([40,30,30], labels=["X","Y","Z"], autopct='%1.1f%%')
axs[1,1].set_title("Pie")

plt.tight_layout()
plt.show()
