# learning about dictionary in python and using json module

import json
import logging

# create a dictionary
data = {
    "weekdays": {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': '6', 'sunday': 7},
    "months": ['Jan', 'feb', 'mar']
}

data_1 = {
    "weekdays": {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': '6', 'sunday': 7},
    "weekdays_2": {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': '6', 'sunday': 7}
}

print(list(data))  # returns all the keys in the dictionary
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
logging.info(list(data))

# Iterating through dictionary
for k, v in data.items():
    print(k, v)

print('-------------1')
for weekday in data:
    print(data[weekday])

print('-------------2')
for key, value in data_1.items():
    print(f'-----> {key}:')
    for info in value:
        print(info + ':' + str(value[info]))

json_file = open('json_file.txt', 'w')  # open file handler/pointer
json.dump(data, json_file, indent=4)
json_file.close()
