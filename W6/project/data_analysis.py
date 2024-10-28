# Added a function to view the maximum and minimum life expectancy by country and the average life expectancy by country.

with open("project/life-expectancy.csv") as life_expectancy:   
    user_year = int(input('Enter the year of interest: '))
    user_country = input('Enter the country of interest: ')
    
    overall_max_years = 0
    overall_max_country = ''
    overall_max_year = 0

    overall_min_years = 9999
    overall_min_country = ''
    overall_min_year = 0

    max_years = 0
    max_country = ''

    min_years = 99999
    min_country = ''

    country_min = 9999
    country_max = 0
    country_num_values = 0
    country_total = 0

    num_of_values = 0
    total = 0

    next(life_expectancy)

    for data in life_expectancy:
        parts = data.strip().split(",")

        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_years = float(parts[3])

        if life_years > overall_max_years:
            overall_max_years = life_years
            highest_country = country
            year_for_highest = year

        if life_years < overall_min_years:
            overall_min_years = life_years
            lowest_country = country
            year_for_lowest = year
        
        if user_year == year:
            total += life_years
            num_of_values += 1
            if life_years < min_years:
                min_years = life_years
                min_country = country

            if life_years > max_years:
                max_years = life_years
                max_country = country

        if user_country.lower() == country.lower():
            country_num_values += 1
            country_total += life_years
            if life_years < country_min:
                country_min = life_years

            if life_years > country_max:
                country_max = life_years
    
    country_average = country_total / country_num_values if country_num_values > 0 else 0
    average = total / num_of_values if num_of_values > 0 else 0

print(f"\nThe overall max life expectancy is: {overall_max_years} from {highest_country} in {year_for_highest}")
print(f"The overall min life expectancy is: {overall_min_years} from {lowest_country} in {year_for_lowest}")
print()
print(f"For the year {user_year}:")
print(f"The average life expectancy across all countries was {average:.2f}")
print(f"The max life expectancy was in {max_country} with {max_years}")
print(f"The min life expectancy was in {min_country} with {min_years}")
print()
print(f"For the country {user_country.capitalize()}:")
print(f"The average life expectancy in this country is: {country_average:.2f}")
print(f"The max life expectancy was {country_max}")
print(f"The min life expectancy was {country_min}")