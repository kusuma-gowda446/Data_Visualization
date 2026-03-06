import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.linspace(0,5,11)
y=x**2
# plt.scatter(x,y)
# plt.show()
# plt.hist(x)
# plt.show()
# plt.boxplot(x)
# plt.show()

fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
plt.show()
plt.savefig("basic.png")