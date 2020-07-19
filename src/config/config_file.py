import os
import json


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, r'../../../../credentials.json')


def database_config():
    with open(filename, 'r') as json_file:
        data = json.loads(json_file.read())

    data = [
        data.get('data').get('user'),
        data.get('data').get('password'),
        data.get('data').get('host'),
        data.get('data').get('port'),
        data.get('data').get('database')
    ]
    return data
