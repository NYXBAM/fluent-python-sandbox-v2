import typing

class City(typing.NamedTuple):
    continent: str
    name: str
    country: str
    
cities = [
    City("Asia", "Tokyo", "JP"),
    City("Asia", "Delhi", "IN"),
    City("North America", "Mexico City", "MX"),
    City("North America", "New York", "US"),
    City("South America", "São Paulo", "BR"),
]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
                
    return results

def match_asian_countries():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia', country=country):
                results.append(country)
                
    return results


def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            case City(continent='Asia'):
                results.append(city)
                
    return results


def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):
                results.append(country)
                
    return results

print(match_asian_cities()) # [City(continent='Asia', name='Tokyo', country='JP'), 
                            # City(continent='Asia', name='Delhi', country='IN')]
print(match_asian_countries()) # ['JP', 'IN']

print(match_asian_cities_pos())

print(match_asian_countries_pos())

print(City.__match_args__) # ('continent', 'name', 'country')