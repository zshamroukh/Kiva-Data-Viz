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

#Based on the data, what kind of recommendations can you make to Kiva about the loans they give?
#What actions could be taken to implement the recommendations you've made?

# Creating Box Plot of Loan Amount Distribution by Country
plt.figure(figsize=(16, 10))
sns.boxplot(data = df, x = 'country', y = 'loan_amount')
plt.title('Loan Amount Distribution by Country')

#Which country's box has the widest distribution?
#In which country would you be most likely to receive the largest loan amount?

# Creating Box Plot of Loan Amount Distribution by Activity
plt.figure(figsize=(16, 10))
sns.boxplot(data = df, x = 'activity', y = 'loan_amount')
plt.title('Loan Amount Distribution by activity')

#What does this visualization reveal that previous ones did not?

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

#What does this visualization reveal about the distribution of loan amounts within countries by gender?