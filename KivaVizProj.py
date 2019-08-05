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
barplot_graph = sns.barplot(data = df, x = 'country', y = 'loan_amount', hue = 'gender')

# Style the figure
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

sns.set_palette('Dark2')
sns.set_style('darkgrid')

barplot = barplot_graph.get_figure()
barplot.savefig('barplot.png') 

# Create figure and axes
plt.figure(figsize=(25, 15))
ax.set_title('Average Kiva Loans By Gender & Country')

# Creating Box Plot of Loan Amount Distribution by Country
plt.figure(figsize=(16, 10))
boxplot_c_graph = sns.boxplot(data = df, x = 'country', y = 'loan_amount')
plt.title('Loan Amount Distribution by Country')

boxplot_c = boxplot_c_graph.get_figure()
boxplot_c.savefig('boxplot_c.png') 

# Creating Box Plot of Loan Amount Distribution by Activity
plt.figure(figsize=(16, 10))
boxplot_a_graph = sns.boxplot(data = df, x = 'activity', y = 'loan_amount')
plt.title('Loan Amount Boxplot by activity')

boxplot_a = boxplot_a_graph.get_figure()
boxplot_a.savefig('boxplot_a.png')

# Creating Violin Plot of Loan Amount Distribution by Activity
plt.figure(figsize=(16, 10))
violin_a_graph = sns.violinplot(data=df, x="activity", y="loan_amount")
plt.title('Loan Amount Violin Distribution by activity')

violin_a = violin_a_graph.get_figure()
violin_a.savefig('violin_a.png')

# Creating Violin Plot of Loan Amount Distribution by Country
plt.figure(figsize=(16, 10))
violin_c_graph = sns.violinplot(data=df, x="country", y="loan_amount")
plt.title('Loan Amount Violin Distribution by country')

violin_c = violin_c_graph.get_figure()
violin_c.savefig('violin_c.png')

# Some styling
sns.set_palette("Spectral")
plt.figure(figsize=(18, 12))

#Violin Plot of Loans by Country and Gender
vp_country_gender = sns.violinplot(data=df, x="country", y="loan_amount", hue = 'gender', split = True)
plt.title('Loan Amount Violin Distribution by country and gender')
vp_c_g = vp_country_gender.get_figure()
vp_c_g.savefig('violin_c_g.png') 


