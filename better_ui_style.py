import matplotlib.pyplot as plt

plt.style.use('ggplot')  # try: seaborn, dark_background

x = [1,2,3,4,5]
y = [5,7,8,6,9]

plt.figure(figsize=(8,5))
plt.plot(x, y, marker='o')

plt.title("Modern Styled Graph")
plt.show()
