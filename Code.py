import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
tips
tips.describe()
tips.info()
tips.isnull().sum()
~tips.duplicated()
df1=tips[~tips.duplicated()]
df1
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, linewidth=2, width=0.6, boxprops={"facecolor": "lightblue", "edgecolor": "darkblue"},
            whiskerprops={"color": "black", "linestyle": "--", "linewidth": 1.5 },
            capprops={"color": "black", "linestyle": "--", "linewidth": 1.5})
sns.barplot(x=tips['day'], y=tips['total_bill'],hue=tips['sex'])
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()
avg_tip = tips.groupby('smoker')['tip'].mean()
p1= plt.bar(avg_tip.index, avg_tip, label='Tip', width=0.4)
plt.title('Average tip amount given by smokers and non-smokers')
plt.show()
tips["tip_per"] = tips["tip"] / tips["total_bill"]
sns.scatterplot(x="size", y="tip_per", data=tips)
plt.title("Tip Percentage by Dining Party Size")
plt.show()
states=tips.loc[:,["sex","tip"]]
states=states.groupby(by=["sex"]).sum().sort_values(by="tip")
sns.barplot(x=states.index,y="tip",data=states)
plt.xlabel=("Sex")
plt.ylabel=("Tips")
plt.show()
sns.histplot(data=tips, x="total_bill", hue="time", element="step", stat="density")
plt.title("Distribution of Total Bill Amounts by Time of Day")
plt.show()
sns.relplot(data=tips,x=tips["time"],y=tips["total_bill"],hue="time")
avg_total_bill = tips.groupby('size')['total_bill'].mean()
p1 = plt.bar(avg_total_bill.index, avg_total_bill, label='Total Bill', width=0.4)
plt.title('Average Total bill amount given by Dining Party Size')
plt.show()
sns.relplot(data=tips,x="day",y="tip",hue="day")
sns.barplot(x=tips['time'], y=tips['tip'])
plt.xlabel=("Service")
plt.ylabel=("Tips")
plt.show()
tips.corr()
sns.heatmap(tips.corr(),annot=True)
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Correlation between Tip Amount and Total Bill Amount")
plt.show()
