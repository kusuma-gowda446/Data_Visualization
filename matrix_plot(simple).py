import matplotlib.pyplot as plt
import numpy as np

# create a 5x5 matrix
data = np.array([
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9]
])

plt.imshow(data, cmap='viridis')
plt.colorbar()

plt.title("Matrix Plot Example")
plt.xlabel("Columns")
plt.ylabel("Rows")

plt.show()
