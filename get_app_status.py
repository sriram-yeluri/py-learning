import requests
import logging
import json
from termcolor import colored


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
    print(f'<-------------------------- Status Begin ------------>')
    status = ''
    for key, value in json_data.items():
        print(f'{key} >>>>>>>>>>>>>>>>')
        for index in range(len(value)):
            for url in value[index]:
                # print(value[index][url])
                print(f'{url}:')
                try:
                    resp = requests.get(value[index][url])
                    if resp.status_code == 200:
                        status = 'ACTIVE'
                        print(colored(f'{status}', 'green'))
                    else:
                        status = 'OFF_LINE'
                        print(colored(f':{status}', 'red'))
                except requests.exceptions.RequestException as e:
                    print(colored('exception:', 'red'), e)

    print(f'<-------------------------- Status End ------------>')


app_urls_json = read_file_to_json('app_urls.json')
if app_urls_json:
    get_app_status(app_urls_json)
