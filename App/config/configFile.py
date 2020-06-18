import json

def databaseConfig():

    with open('C:/Users/guiyo/Desktop/IC02-2019-Painel-de-Dados-Covid19/Config.json', 'r') as json_file:
        data = json.loads(json_file.read())

    data = [
        data.get('data').get('user'),
        data.get('data').get('password'),
        data.get('data').get('host'),
        data.get('data').get('port'),
        data.get('data').get('database')
        ]

    return data