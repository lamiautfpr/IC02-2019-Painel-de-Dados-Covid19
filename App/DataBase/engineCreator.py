from config import configFile
from sqlalchemy import create_engine

conf = configFile.databaseConfig()


def engineDb():

    engine = create_engine(
        'postgresql://{}:{}@{}:{}/{}'.format(
            conf[0],
            conf[1],
            conf[2],
            conf[3],
            conf[4]
        ), echo=True)

    return engine
