minimum = 9999
minimum_country = ''
minimum_year = 0
maximum = 0
maximum_country = ''
maximum_year = 0 

age_list = []
spec_min_age = 9999
spec_min_country = ''
spec_max_age = 0 
spec_max_country = ''

# you don't need to use strip metod in input
selected_year = int(input('please, enter the year of interest: '))

with open('project\life-expectancy.csv') as le:

# function next skips the first line and goes to the next
    next(le)

    for line in le: 
# you just need to create 1 variable to split ang clean your lines
        parts = line.strip().split(',')
        country = parts[0] 
        year = int(parts[2])
        age = float(parts[3])

        if age < minimum:
            minimum = age 
            minimum_country = country
            minimum_year = year

        if age > maximum:
            maximum = age 
            maximum_country = country
            maximum_year = year 

        if year == selected_year:
            age_list.append(age)       

            if age < spec_min_age:
                spec_min_age = age
                spec_min_country = country
            if age > spec_max_age:
                spec_max_age = age
                spec_max_country = country

spec_avg = sum(age_list) / len(age_list)   

print(f'\nThe overall max life expectancy is:{maximum} from {maximum_country} in {maximum_year}')
print(f'The overall min life expectancy is: {minimum} from {minimum_country} in {minimum_year}')

print(f'\nFor the year {selected_year}:')
print(f'The average life expectancy across all contries was {spec_avg:.2f}')
print(f'The max life expectancy was in {spec_max_country} with {spec_max_age}')
print(f'The min life expectancy was in {spec_min_country} with {spec_min_age}')