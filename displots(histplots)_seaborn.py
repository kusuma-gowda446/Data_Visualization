import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset 
df=sns.load_dataset("tips")
print(df)

# insted of displot we can alos use histplot to plot the histogram of the datq
sns.displot(df['total_bill'])
plt.show()


# we can plot 2 vales in the same graph by using subplots now lets draw for tips and total bills
plt.subplot(1,2,1)
sns.histplot(df["total_bill"])
plt.subplot(1,2,2)
sns.histplot(df['tip'])
plt.show()







