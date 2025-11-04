# Function to read the CSV file and return data as a list of dictionaries
def read_file():
    with open('life-expectancy.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]  # Skip the header
    data = []
    for line in lines:
        parts = line.strip().split(',')
        data.append({
            'year': int(parts[0]),
            'country': parts[1],
            'life_expectancy': float(parts[2])
        })
    return data

# Function to find the year and country with the lowest life expectancy
def lowest_life_expectancy(data):
    lowest = min(data, key=lambda x: x['life_expectancy'])
    return lowest['year'], lowest['country'], lowest['life_expectancy']

# Function to find the year and country with the highest life expectancy
def highest_life_expectancy(data):
    highest = max(data, key=lambda x: x['life_expectancy'])
    return highest['year'], highest['country'], highest['life_expectancy']

# Function to calculate the average life expectancy for a specific year
def average_for_year(data, year):
    year_data = [d for d in data if d['year'] == year]
    if not year_data:
        return None
    total = sum(d['life_expectancy'] for d in year_data)
    return total / len(year_data)

# Function to find the country with the lowest and highest life expectancy for a year
def extremes_for_year(data, year):
    year_data = [d for d in data if d['year'] == year]
    if not year_data:
        return None, None
    lowest = min(year_data, key=lambda x: x['life_expectancy'])
    highest = max(year_data, key=lambda x: x['life_expectancy'])
    return lowest, highest

# Main function
def main():
    data = read_file()
    
    # Task 1: Lowest life expectancy
    year_low, country_low, life_low = lowest_life_expectancy(data)
    print(f'Lowest life expectancy: {life_low} in {country_low} in {year_low}')
    
    # Task 2: Highest life expectancy
    year_high, country_high, life_high = highest_life_expectancy(data)
    print(f'Highest life expectancy: {life_high} in {country_high} in {year_high}')
    
    # Task 3: User input for a specific year
    user_year = int(input('Enter a year of interest: '))
    average = average_for_year(data, user_year)
    if average is None:
        print(f'No data available for the year {user_year}.')
    else:
        print(f'Average life expectancy in {user_year}: {average:.2f}')
        lowest, highest = extremes_for_year(data, user_year)
        if lowest and highest:
            print(f'Country with lowest life expectancy: {lowest["country"]} ({lowest["life_expectancy"]})')
            print(f'Country with highest life expectancy: {highest["country"]} ({highest["life_expectancy"]})')

if __name__ == '__main__':
    main()
