import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.linspace(0,5,11)
# print(x)
y=x**2
# print(y)

                #   it plots the graph of x against y 
plt.plot(x,y) 
plt.title("x-y_graph") 
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()



