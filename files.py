# script to read json file

import json

# read file
with open('sample.json', 'r') as json_file:
    data = json_file.read()

# parse file
obj = json.loads(data)

# show values
# print("userId: " + str(obj['users'][0]['userId']))
# print("firstname: " + str(obj['users'][0]['firstName']))
# print("lastname: " + str(obj['users'][0]['lastName']))
print(obj['users'])

# Write to json file
with open('json_response.txt', 'w') as json_file:
    json.dump(obj, json_file, indent=4)  # Pretty Printing JSON string back
