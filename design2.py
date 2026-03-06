import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

fig, ax = plt.subplots(figsize=(12,6))

# Line with circle markers
ax.plot(x, y1, color="blue", lw=2, marker="o", markersize=5, label="sin(x)")

# Dashed line with square markers
ax.plot(x, y2, color="green", lw=2, ls="--", marker="s", markersize=5, label="cos(x)")

# Thick dotted line
ax.plot(x, y3, color="purple", lw=3, ls=":", label="sin(x)+cos(x)")

# Fill area between curves
ax.fill_between(x, y1, y2, color="orange", alpha=0.3)

# Grid and styling
ax.set_title("Unique Line Design Example")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.grid(True, linestyle="--", alpha=0.5)

ax.legend()

plt.show()
