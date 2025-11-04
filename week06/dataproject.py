
def read_file():

    with open('life-expectancy.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines = lines[1:]
    
    data = []
    

    for line in lines:
        line = line.strip()
        
        parts = line.split(',')
        record = {
            'year': int(parts[0]),                
            'country': parts[1],                
            'life_expectancy': float(parts[2])  
        }
        
        data.append(record)
    
    return data


def find_lowest(data):

    lowest = min(data, key=lambda x: x['life_expectancy'])
    return lowest

def find_highest(data):

    highest = max(data, key=lambda x: x['life_expectancy'])
    return highest

def average_for_year(data, year):

    year_data = [record for record in data if record['year'] == year]

    if len(year_data) == 0:
        return None

    total = sum(record['life_expectancy'] for record in year_data)

    average = total / len(year_data)
    
    return average

def extremes_for_year(data, year):

    year_data = [record for record in data if record['year'] == year]

    if len(year_data) == 0:
        return None, None

    lowest = min(year_data, key=lambda x: x['life_expectancy'])
    highest = max(year_data, key=lambda x: x['life_expectancy'])
    
    return lowest, highest

def main():

    data = read_file()

    lowest = find_lowest(data)
    print(f"\nLowest life expectancy: {lowest['life_expectancy']} in {lowest['country']} ({lowest['year']})")

    highest = find_highest(data)
    print(f"Highest life expectancy: {highest['life_expectancy']} in {highest['country']} ({highest['year']})")

    user_year = int(input("\nEnter a year you want to analyze: "))

    average = average_for_year(data, user_year)

    if average is None:
        print(f"Sorry, there is no data for the year {user_year}.")
    else:

        print(f"\nAverage life expectancy in {user_year}: {average:.2f}")

        lowest_year, highest_year = extremes_for_year(data, user_year)
        
        print(f"Lowest in {user_year}: {lowest_year['country']} ({lowest_year['life_expectancy']})")
        print(f"Highest in {user_year}: {highest_year['country']} ({highest_year['life_expectancy']})")

if __name__ == "__main__":
    main()
