from config.config_file import database_config
from sqlalchemy import create_engine

data = database_config()


def engine_db():
    engine = create_engine(
        'postgresql://{}:{}@{}:{}/{}'.format(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4]
        ), echo=False)
    return engine
