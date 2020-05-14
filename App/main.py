from Scripts.Brasil_io import get_brasilio, get_cartorio
from Scripts.Brasil_api import get_brasilapi, get_mundo
from DataBase.engineCreator import engineDb
from sqlalchemy.orm import sessionmaker

# Create session
Session = sessionmaker(bind=engineDb())
session = Session()

# Brasil.apiNacional
get_brasilapi.insertData(session)
# Brasil.ioMundial
get_mundo.insertData(session)

session.Close()
