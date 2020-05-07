from App.config.configFile import databaseConfig
from sqlalchemy import create_engine

conf = databaseConfig()


def engineDb():

    engine = create_engine(
        'postgresql://{}:{}@localhost:{}/{}'.format(
            conf[0],
            conf[1],
            conf[2],
            conf[3]
        ), echo=False)

    return engine
