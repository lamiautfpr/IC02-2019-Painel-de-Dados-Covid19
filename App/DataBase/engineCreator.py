from config import configFile
from sqlalchemy import create_engine

data = configFile.databaseConfig()

def engineDb():

    engine = create_engine(
        'postgresql://{}:{}@{}:{}/{}'.format(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4]
        ), echo=False)

    return engine
