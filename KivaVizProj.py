from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns

df = pd.read_csv(r'C:\Users\zsham\Desktop\Pywork\Data\kiva_data.csv')
print(df.head(25))

avg_loan_by_gender = df.groupby('gender').mean().round(2).reset_index()
print(avg_loan_by_gender)

#Which country has the least disparity in loan amounts awarded by gender?
avg_loan_by_gender_country = df.groupby(['country', 'gender']).mean().round(2).reset_index()
print(avg_loan_by_gender_country)


# Creating Bar Plot of Loan Amount by country and gender
f, ax = plt.subplots(figsize=(15, 10))
sns.barplot(data = df, x = 'country', y = 'loan_amount', hue = 'gender')

# Style the figure
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

sns.set_palette('Dark2')
sns.set_style('darkgrid')

# Create figure and axes
plt.figure(figsize=(25, 15))
ax.set_title('Average Kiva Loans By Gender & Country')

# Creating Box Plot of Loan Amount Distribution by Country
plt.figure(figsize=(16, 10))
sns.boxplot(data = df, x = 'country', y = 'loan_amount')
plt.title('Loan Amount Distribution by Country')

# Creating Box Plot of Loan Amount Distribution by Activity
plt.figure(figsize=(16, 10))
sns.boxplot(data = df, x = 'activity', y = 'loan_amount')
plt.title('Loan Amount Distribution by activity')

# Creating Violin Plot of Loan Amount Distribution by Activity
plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="activity", y="loan_amount")

# Creating Violin Plot of Loan Amount Distribution by ountry
plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="country", y="loan_amount")

# Some styling (feel free to modify)
sns.set_palette("Spectral")
plt.figure(figsize=(18, 12))
sns.violinplot(data=df, x="country", y="loan_amount", hue = 'gender', split = True)