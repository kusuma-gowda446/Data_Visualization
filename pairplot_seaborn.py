import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset 
df=sns.load_dataset("tips")

# hue represents the vlues in different color based on the vale passed in hue parameter
# we can use palette to change the color of the graph
sns.pairplot(df,hue='sex')
plt.show()

sns.pairplot(df,hue='size',palette='rainbow')
plt.show()


