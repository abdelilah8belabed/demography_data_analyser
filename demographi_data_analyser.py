import pandas as pd
import warnings


def demographi_():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=FutureWarning)
        data = pd.read_csv('adult.data.csv')

        # Fill missing values: age by mean, occupation by mode
        data['age'] = data['age'].fillna(data['age'].mean())
        data['hours-per-week'] = data['hours-per-week'].fillna(data['hours-per-week'].mean())
        data['capital-loss'] = data['capital-loss'].fillna(data['capital-loss'].mean())
        data['fnlwgt'] = data['fnlwgt'].fillna(data['fnlwgt'].mean())
        data['capital-gain'] = data['capital-gain'].fillna(data['capital-gain'].mean())
        data['occupation'] = data['occupation'].fillna(data['occupation'].mode()[0])
        # Count occurrences of each race
        race = [pd.value_counts(data['race'])]

        # Calculate average age of men
        men = data[data['sex'] == 'Male']
        average_age = round(men['age'].mean(), 1)

        # Calculate percentage of people with Bachelor's degrees
        bachelor = data[data['education'] == 'Bachelors'].shape[0]
        total_degrees = data['education'].shape[0]
        bachelor_percentage = round((bachelor / total_degrees) * 100, 1)

        # Calculate percentage of people with advanced degrees earning more than 50K
        adv_degree = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
        adv_degree_50 = adv_degree[adv_degree['salary'] == '>50K']
        num_of_adv_degree = adv_degree.shape[0]
        num_of_adv_degree_50 = adv_degree_50.shape[0]
        percentage_adv_50 = round((num_of_adv_degree_50 / num_of_adv_degree) * 100, 1)

        # Calculate percentage of people without advanced education earning more than 50K
        no_degree = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
        no_degree_50 = no_degree[no_degree['salary'] == '>50K']
        num_no_degree = no_degree.shape[0]
        num_no_degree_50 = no_degree_50.shape[0]
        percentage_no_degree_50 = round((num_no_degree_50 / num_no_degree) * 100, 1)

        # Find minimum number of hours worked per week
        min_hours = data['hours-per-week'].min()

        # Calculate percentage of people working minimum hours who earn more than 50K
        people_min_hours = data[data['hours-per-week'] == min_hours]
        people_min_hours_50 = people_min_hours[people_min_hours['salary'] == '>50K']
        num_of_people = people_min_hours.shape[0]
        num_of_people_50 = people_min_hours_50.shape[0]
        percentage_min_hours_high_salary = round((num_of_people_50 / num_of_people) * 100, 1)

        # Find country with highest percentage of people earning more than 50K
        salary_more_than_50 = data[data["salary"] == '>50K']
        countries_with_salary_more_than_50 = salary_more_than_50['native-country'].value_counts()
        all_countrys_with_50K = countries_with_salary_more_than_50.sum()
        best = countries_with_salary_more_than_50.max()
        purcentage_of_most_country_50 = round((best / all_countrys_with_50K) * 100, 1)
        wich_is = countries_with_salary_more_than_50.idxmax()

        # Find the most popular occupation for those who earn >50K in India
        most_salary_more_than_50_india = salary_more_than_50[salary_more_than_50['native-country'] == 'India']
        most_popular_occupation_india_50 = most_salary_more_than_50_india['occupation'].value_counts().idxmax()

    return {
        'race_count': race,
        'average_age': average_age,
        'percentage_of_people_they have_bac': bachelor_percentage,
        'percentage_people_with_high-degree__they_make_more_than 50k': percentage_adv_50,
        'min_hours_that__a-person_work': min_hours,
        'percentage_min_hours_high_salary': percentage_min_hours_high_salary,
        'highest_country_with_salary_more_than_50k': wich_is,
        'percentage_country_with_salary_more_than_50k': purcentage_of_most_country_50,
        'most_popular_occupation_india_that_give_50k': most_popular_occupation_india_50
    }


results = demographi_()
for key, value in results.items():
    print(f"{key}: {value}")