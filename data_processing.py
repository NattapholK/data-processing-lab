import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()


def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    result = []
    for item in dict_list:
        if condition(item):
            result.append(item)
    return result

#Enter your code


def aggregate(aggregation_key, aggregation_function, dict_list):
    
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    values = []
    for item in dict_list:
        val = item[aggregation_key]
        try:
            val = float(val)  # ลองแปลงเป็น float ถ้าทำได้ (อุณหภูมิ, ตัวเลข)
        except ValueError:
            pass             # ถ้าแปลงไม่ได้ ให้ใช้ค่าเดิม (ชื่อประเทศ, ข้อความ)
        values.append(val)
        
    return aggregation_function(values)
    # YOUR CODE HERE


# Print the average temperature of all the cities
print(f"average temperature of all the cities :{aggregate('temperature',lambda tem: sum(tem)/len(tem),cities)}")

# Print all cities in Germany

print(filter_items(lambda item: item["country"] == "Germany",cities))

# Print all cities in Spain with a temperature above 12°C
print("cities in Spain with a temperature above 12°C")
print(filter_items(lambda item: item["country"] == "Spain" 
                   and float(item["temperature"]) > 12,cities))

# Count the number of unique countries

unique_countries_count = aggregate("country", lambda countries: len(set(countries)), cities)
print(unique_countries_count)

# Print the average temperature for all the cities in Germany
german_cities = [city for city in cities if city["country"] == "Germany"]
avg_temp_germany = aggregate(
    "temperature", 
    lambda temp: sum(temp) / len(temp), 
    german_cities
)
print("average temperature in germany", avg_temp_germany)

# Print the max temperature for all the cities in Italy

italy_cities = [city for city in cities if city["country"] == "Italy"]
avg_temp_Italy = aggregate(
    "temperature", 
    max, 
    italy_cities
)
print("Max temperature in Italy", avg_temp_Italy)

