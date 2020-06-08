import json
import os

def databaseConfig():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(path,'Config.json'), 'r') as json_file:
        data = json.loads(json_file.read())

    return ([
            data.get('data').get('user'),
            data.get('data').get('password'),
            data.get('data').get('host'),
            data.get('data').get('port'),
            data.get('data').get('database'),
            ])
