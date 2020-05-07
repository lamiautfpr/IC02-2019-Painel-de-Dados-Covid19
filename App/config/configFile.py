def databaseConfig():
    user = 'postgres'
    password = 'root'
    port = '5432'
    database = 'postgres'
    return [user, password, port, database]


def urlGeneretor(var, date):
    if var is 1:
        # Brasil.io --- Dados Brasil
        url = ('https://brasil.io/api/dataset/covid19/caso/data/?date<{}'
               .format(date))
    elif var is 2:
        # Brasil.io --- Dados Cartórios
        pass
    elif var is 3:
        # Brasil.api
        pass
    elif var is 4:
        # Brasil.api
        pass
    else:
        # ERROR
        pass

    return url
