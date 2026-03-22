import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length):
    if length < 1:
        return
    
    x2 = x + length * np.cos(angle)
    y2 = y + length * np.sin(angle)
    
    plt.plot([x, x2], [y, y2], color='brown')
    
    draw_tree(x2, y2, angle + np.pi/6, length * 0.7)
    draw_tree(x2, y2, angle - np.pi/6, length * 0.7)

draw_tree(0, 0, np.pi/2, 10)

plt.title("Fractal Tree")
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
