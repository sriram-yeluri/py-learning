import requests
import logging
import json


def read_file_to_json(file_name):
    try:
        with open(file_name, 'r') as fp:
            data = fp.read()
        return json.loads(data)
    except FileNotFoundError:
        print('FileNotFoundError Occurred')
        logging.error('FileNotFoundError Occurred')
    return None


def get_app_status(json_data):
    print(f'-------------------------- Status Begin ------------')
    status = 'OFF_LINE'
    for key, value in json_data.items():
        for index in range(len(value)):
            for url in value[index]:
                # print(value[index][url])
                print(f'{key}:{url}')
                try:
                    resp = requests.get(value[index][url])
                except Exception as err:
                    print(err)
                if resp.status_code == 200:
                    status = 'ACTIVE'
                print(f':{status}')

    print(f'-------------------------- Status End ------------')


app_urls_json = read_file_to_json('app_urls.json')
if app_urls_json:
    get_app_status(app_urls_json)