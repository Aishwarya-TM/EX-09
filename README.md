# EX-09 Data-Visualization

# AIM:
  To Perform Data Visualization on a complex dataset and save the data to a file.
# EXPLANATION:
  Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.
# ALGORITHM:
## STEP-1:
  Read the given Data.
## STEP-2:
  Clean the Data Set using Data Cleaning Process.
## STEP-3:
  Apply Feature generation and selection techniques to all the features of the data set.
## STEP-4:
  Apply data visualization techniques to identify the patterns of the data.
# CODE:
import seaborn as sns

import pandas as pd

import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

tips

## Data Cleaning Process:
tips.describe()

tips.info()

tips.isnull().sum()

~tips.duplicated()

df1=tips[~tips.duplicated()]

df1

sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, linewidth=2, width=0.6, boxprops={"facecolor": "lightblue", "edgecolor": "darkblue"},
            whiskerprops={"color": "black", "linestyle": "--", "linewidth": 1.5 },
            capprops={"color": "black", "linestyle": "--", "linewidth": 1.5})

## Day of the week has the highest total bill amount:
sns.barplot(x=tips['day'], y=tips['total_bill'],hue=tips['sex'])

plt.xlabel('Day of the Week')

plt.ylabel('Total Bill')

plt.show()

## Average tip amount given by smokers and non-smokers:
avg_tip = tips.groupby('smoker')['tip'].mean()

p1= plt.bar(avg_tip.index, avg_tip, label='Tip', width=0.4)

plt.title('Average tip amount given by smokers and non-smokers')

plt.show()

## Tip percentage vary based on the size of the dining party:
tips["tip_per"] = tips["tip"] / tips["total_bill"]

sns.scatterplot(x="size", y="tip_per", data=tips)

plt.title("Tip Percentage by Dining Party Size")

plt.show()

## Gender tends to leave higher tips:
states=tips.loc[:,["sex","tip"]]

states=states.groupby(by=["sex"]).sum().sort_values(by="tip")

sns.barplot(x=states.index,y="tip",data=states)

plt.xlabel=("Sex")

plt.ylabel=("Tips")

plt.show()

## Relationship between the total bill amount and the day of the week:
sns.histplot(data=tips, x="total_bill", hue="time", element="step", stat="density")

plt.title("Distribution of Total Bill Amounts by Time of Day")

plt.show()

## Distribution of total bill amounts vary across different time periods:
sns.relplot(data=tips,x=tips["time"],y=tips["total_bill"],hue="time")

## Dining party size group tends to have the highest average total bill amount:
avg_total_bill = tips.groupby('size')['total_bill'].mean()

p1 = plt.bar(avg_total_bill.index, avg_total_bill, label='Total Bill', width=0.4)

plt.title('Average Total bill amount given by Dining Party Size')

plt.show()

## Distribution of tip amounts for each day of the week:
sns.relplot(data=tips,x="day",y="tip",hue="day")

## Tip amount vary based on the type of service:
sns.barplot(x=tips['time'], y=tips['tip'])

plt.xlabel=("Service")

plt.ylabel=("Tips")

plt.show()

## Correlation between the total bill amount and the tip amount:
tips.corr()

sns.heatmap(tips.corr(),annot=True)

sns.scatterplot(x="total_bill", y="tip", data=tips)

plt.title("Correlation between Tip Amount and Total Bill Amount")

plt.show()

# OUTPUT:
![Screenshot (73)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/b36a21ab-1a02-44ac-a5ec-8a302f3fbfe8)

## Data Cleaning Process:
![Screenshot (74)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/1913e2a6-8c31-4cbe-86bb-2d5a4366b8ef)

![Screenshot (75)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/c7152f1c-aaba-4a54-a798-008cba864569)

![Screenshot (76)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/d99a83f3-7bfa-45a5-bfd8-56db964bd3e3)

![Screenshot (77)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/0ac899fe-c85e-4c5b-9d62-163b68d0105d)

![Screenshot (78)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/3364907e-6c48-4678-8aba-ab53b10ad579)

## Day of the week has the highest total bill amount:
![Screenshot (79)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/a6cc0d22-5ce2-4640-b950-06394cc149c6)

## Average tip amount given by smokers and non-smokers:
![Screenshot (80)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/81ae07d1-a0a4-4d07-870f-e4934e168e31)

## Tip percentage vary based on the size of the dining party:
![Screenshot (81)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/361f1cd2-b4d1-4ece-bb22-e9873a24f6fc)

## Gender tends to leave higher tips:
![Screenshot (82)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/63900c81-29b5-4300-b730-376cbe4c7678)

## Relationship between the total bill amount and the day of the week:
![Screenshot (91)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/09d3789f-05c9-4999-98c6-2a4fe47e84c8)

## Distribution of total bill amounts vary across different time periods:
![Screenshot (84)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/b2f0908b-5c07-4ec8-8243-21d36f1a3944)

## Dining party size group tends to have the highest average total bill amount:
![Screenshot (85)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/e79c04c9-c083-4e15-bf23-60a702d17f3e)

## Distribution of tip amounts for each day of the week:
![Screenshot (86)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/0b9bb00e-c798-4304-aade-766533be46fc)

## Tip amount vary based on the type of service:
![Screenshot (87)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/b8a7f5c4-d802-44f8-8883-1ac60c915175)

## Correlation between the total bill amount and the tip amount:
![Screenshot (88)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/485a4874-469c-46ea-bf5f-de010a565b93)

![Screenshot (89)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/b7ec6ecc-05c1-4a6e-ac68-dc0f82c05c48)

![Screenshot (90)](https://github.com/Aishwarya-TM/EX-09/assets/127846109/a68a70b5-66e3-4d67-bf71-475c1ba68870)

# RESULT:
 Thus the Data Visualization techniques were performed for the given dataset and output was verified successfully.
