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

# Print all cities in Germany
for city in cities:
    if city["country"] == "Germany":
        print(city["city"])
'''

Your code here

'''

# Print all cities in Spain with a temperature above 12°C

for city in cities:
    if city["country"] == "Spain" and (float(city["temperature"]) > 12):
        print(city["city"])

'''
Your code here

'''

# Count the number of unique countries

count = {}
for city in cities:
    if city["country"] not in count:
        count[city["country"]] = 1
    else:
        count[city["country"]] += 1 

count_country = 0
for country in count:
    count_country += 1
print(count_country)
'''
Your code here

'''


# Print the average temperature for all the cities in Germany
print("average temperature for all the cities in Germany")
print()
german_count = []
for city in cities:
    if city["country"] == "Germany":
        german_count.append(float(city["temperature"]))
print(f'average temperature in german :{sum(german_count)}/{len(german_count)}')
'''
Your code here

'''
print()
# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy")
print()
Italy_count = []
for city in cities:
    if city["country"] == "Italy":
        Italy_count.append(float(city["temperature"]))
print(f"Max {max(Italy_count)}")

'''
Your code here

'''