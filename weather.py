from pprint import pprint

import requests

APIKEY = 'a2187fdd774613eb342624434519ff82'

r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={APIKEY}')
pprint(r.json())

# The formula to convert Kelvin into Celsius is C = K - 273.15
