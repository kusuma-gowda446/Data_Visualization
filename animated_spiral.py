import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_aspect('equal')

line, = ax.plot([], [])

def update(frame):
    t = np.linspace(0, 4*np.pi, 500)
    r = t + frame * 0.1
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=50, interval=100)
plt.show()
