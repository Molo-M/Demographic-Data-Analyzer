import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask = df['sex'] == 'Male'
    males = df[mask]
    average_age_men = males['age'].mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    mask = df['education'] == 'Bachelors'
    bach = df[mask]
    num_bach = bach.shape[0]
    tot_num = df.shape[0]
    percentage_bachelors = (num_bach / tot_num) * 100
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # Higher education salary calculation
    high_edu = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    edu = df[high_edu]
    mask = edu['salary'] == '>50K'
    high_sal = edu[mask].shape[0]
    higher_num = edu.shape[0]
    high_salary = (high_sal / higher_num) * 100
    high_salary = round(high_salary, 1)

    # Lower education salary calculation
    low_edu = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')
    edu = df[low_edu]
    lower_num = edu.shape[0]
    mask = edu['salary'] == '>50K'
    low_sal = edu[mask].shape[0]
    low_sal = (low_sal / lower_num) * 100

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = higher_num
    lower_education = lower_num

    # percentage with salary >50K
    higher_education_rich = round(high_salary, 1)
    lower_education_rich = round(low_sal, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask = df['hours-per-week'] == min_work_hours
    n_df = df[mask]
    num_min_workers = n_df.shape[0]

    mask = df['salary'] == '>50K'
    num_sal = n_df[mask].shape[0]
    rich_percentage = (num_sal/num_min_workers) * 100
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    mask = df['salary'] == '>50K'
    high_df = df[mask]
    all_ctry = df['native-country'].value_counts()
    countries = high_df['native-country'].value_counts()
    all_ctry = (countries / all_ctry) * 100
    all_ctry = all_ctry.reset_index()
    g = all_ctry['native-country'] == all_ctry['native-country'].max()
    c = all_ctry[g]
    c = np.array(c)
    c = c.tolist()
    fin_ctry = c[0]
    highest_earning_country = fin_ctry[0]

    highest_earning_country_percentage = round(fin_ctry[1], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask = high_df['native-country'] == 'India'
    india = high_df[mask]
    popular = india['occupation'].value_counts()
    mst_pop = popular[0:1]
    pop = mst_pop.reset_index()
    pop = np.array(pop['index'])
    pop = pop.tolist()
    top_IN_occupation = pop[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
