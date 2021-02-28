import json
import logging


def read_file_to_json(file_name):
    try:
        with open(file_name, 'r') as fp:
            data = fp.read()
        return json.loads(data)
    except FileNotFoundError:
        print('FileNotFoundError Occurred')
        logging.error('FileNotFoundError Occurred')
    return None


def iterate_through_json(json_data):
    for key, value in json_data.items():
        print(key, value)
        if key == 'address':
            for i in value:
                print(f'{key}:{value[i]}')
        if key == 'phoneNumbers':
            for v in value:
                print(v)


json_data = read_file_to_json('json_example_1.json')  # None will be returned on failure

# Iterate through json file if not None.
if json_data:
    iterate_through_json(json_data)
