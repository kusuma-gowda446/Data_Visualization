import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 50)
y = np.sin(x)

# Create figure
plt.figure(figsize=(10,5))

# Plot line with markers
plt.plot(x, y, linestyle='--', marker='o', linewidth=2)

# Fill area under curve
plt.fill_between(x, y, alpha=0.3)

# Labels and title
plt.title("Creative Sine Wave Design")
plt.xlabel("X Values")
plt.ylabel("Sin(X)")

# Grid style
plt.grid(True, linestyle=':')

# Show plot
plt.show()
