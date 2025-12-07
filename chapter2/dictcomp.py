dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (62, "Indonesia"),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'russia'),
    (1, 'United States'),
    ]

country_dial = {country: code for code, country in dial_codes}
print(country_dial) # {'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'Indonesia': 62, 'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'russia': 7, 'United States': 1}
c = {code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}
print(c)

def dump(**kwargs):
    return kwargs

print(dump(**{'x': 1}, y=2, **{'z':3})) # {'x': 1, 'y': 2, 'z': 3}
print({'a': 0, **{'x':1}, 'y':2, **{'z':3, 'x':4}}) # {'a': 0, 'x': 4, 'y': 2, 'z': 3}

d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
 
print(d1|d2) # {'a': 2, 'b': 4, 'c': 6}

d1|=d2
print(d1) # {'a': 2, 'b': 4, 'c': 6}



