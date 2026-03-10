import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset 
df=sns.load_dataset("tips")

# to compare with 2 values at the same time we can use jointplot 
sns.jointplot(x=df['total_bill'], y=df['tip'])
plt.show()


# we can also use sns.jointplot (x=[total_bill] , y=[tip] ,kind="hex,reg,scatter")to draw the plots 

sns.jointplot(x=df['total_bill'], y=df['tip'] ,kind='hex')
plt.show()

