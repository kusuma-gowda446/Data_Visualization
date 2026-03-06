import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

xaxis = np.linspace(0, 5, 11)

fig, ax = plt.subplots(figsize=(12, 6))

# Different linewidths
ax.plot(xaxis, xaxis + 1, color="red", linewidth=0.25)
ax.plot(xaxis, xaxis + 2, color="red", linewidth=0.50)
ax.plot(xaxis, xaxis + 3, color="red", linewidth=1.00)
ax.plot(xaxis, xaxis + 4, color="red", linewidth=2.00)

# Different linestyles
ax.plot(xaxis, xaxis + 5, color="green", lw=3, linestyle='-')
ax.plot(xaxis, xaxis + 6, color="green", lw=3, linestyle='-.')
ax.plot(xaxis, xaxis + 7, color="green", lw=3, linestyle=':')

# Custom dash
line, = ax.plot(xaxis, xaxis + 8, color="black", lw=1.5)
line.set_dashes([5, 5, 15, 5])  # dash pattern

# Markers
ax.plot(xaxis, xaxis + 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(xaxis, xaxis + 10, color="blue", lw=3, ls='-', marker='o')
ax.plot(xaxis, xaxis + 11, color="blue", lw=3, ls='--', marker='s')
ax.plot(xaxis, xaxis + 12, color="blue", lw=3, ls='--', marker='1')

# Marker size variations
ax.plot(xaxis, xaxis + 13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(xaxis, xaxis + 14, color="purple", lw=1, ls='-', marker='o', markersize=4)

# Marker face color
ax.plot(
    xaxis, xaxis + 15,
    color="purple",
    lw=1,
    ls='-',
    marker='o',
    markersize=8,
    markerfacecolor="red"
)

# Marker edge styling
ax.plot(
    xaxis, xaxis + 16,
    color="purple",
    lw=1,
    ls='-',
    marker='s',
    markersize=8,
    markerfacecolor="yellow",
    markeredgewidth=3,
    markeredgecolor="green"
)

plt.show()
