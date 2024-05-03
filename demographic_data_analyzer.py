import pandas as pd

# Load the CSV data. Assuming your file is named 'census_data.csv'
df = pd.read_csv('census_data.csv')

# How many people of each race are represented in this dataset?
people_by_race = df['race'].value_counts()
print(people_by_race)

# What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)
print(average_age_men)

# What is the percentage of people who have a Bachelor's degree?
bachelors_count = len(df[df['education'] == 'Bachelors'])
total_count = len(df)
percentage_bachelors = (bachelors_count / total_count) * 100).round(1)
print(percentage_bachelors)

# What percentage of people with advanced education make more than 50K?
# What percentage of people without advanced education make more than 50K?
advanced_education = ['Bachelors', 'Masters', 'Doctorate']
high_earners_advanced = df[(df['education'].isin(advanced_education)) & (df['salary'] == '>50K')]
advanced_count = len(df[df['education'].isin(advanced_education)])
percent_advanced_high_earn = (len(high_earners_advanced) / advanced_count * 100).round(1)
print(percent_advanced_high_earn)

high_earners_no_advanced = df[~df['education'].isin(advanced_education) & (df['salary'] == '>50K')]
no_advanced_count = len(df[~df['education'].isin(advanced_education)])
percent_no_advanced_high_earn = (len(high_earners_no_advanced) / no_advanced_count * 100).round(1)
print(percent_no_advanced_high_earn)

# What is the minimum number of hours a person works per week?
min_hours = df['hours-per-week'].min()
print(min_hours)

# What percentage of the people who work the minimum number of hours have a salary of more than 50K?
min_hours_high_earn = df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')]
min_hours_total = len(df[(df['hours-per-week'] == min_hours)])
percentage_min_hours_high_earn = (len(min_hours_high_earn) / min_hours_total * 100).round(1)
print(percentage_min_hours_high_earn)

# What country has the highest percentage of people that earn >50K?
high_earners_by_country = df[df['salary'] == '>50K'].groupby('native-country')['salary'].count()
total_by_country = df['native-country'].value_counts()
percent_high_earners_by_country = (high_earners_by_country / total_by_country * 100).round(1)
country_highest_percent = percent_high_earners_by_country.idxmax()
highest_percentage = percent_high_earners_by_country.max()
print(f"{country_highest_percent}: {highest_percentage}%")

# Identify the most popular occupation for those who earn >50K in India.
india_high_earners = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
most_popular_occupation = india_high_earners['occupation'].mode()[0]
print(most_popular_occupation)
