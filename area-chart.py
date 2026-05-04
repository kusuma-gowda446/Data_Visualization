import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri"]
hours = [2, 3, 4, 3, 5]

plt.figure(figsize=(8,5))
plt.fill_between(days, hours, alpha=0.3)
plt.plot(days, hours, marker='o')

plt.title("Study Progress")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.show()
