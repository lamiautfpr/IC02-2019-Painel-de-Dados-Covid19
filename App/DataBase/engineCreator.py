from sqlalchemy import create_engine

user = 'postgres'
password = 'root'
port = '5432'
database = 'postgres'


def engineDb():

    engine = create_engine(
        'postgresql://{}:{}@localhost:{}/{}'.format(user,
                                                    password,
                                                    port,
                                                    database
                                                    ), echo=False)

    return engine
