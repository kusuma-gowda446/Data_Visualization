import matplotlib.pyplot as plt

# Data
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = [85, 78, 92, 74, 88]

# Create figure
plt.figure(figsize=(10,6))

# Bar chart
bars = plt.bar(subjects, marks)

# Title and labels
plt.title("Student Marks in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Add values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, str(height),
             ha='center', va='bottom')

# Grid on Y axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()
