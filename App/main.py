from Scripts.Brasil_io import get_brasilio, get_cartorio
from Scripts.Brasil_api import get_brasilapi, get_mundo
from DataBase.engineCreator import engineDb
from sqlalchemy.orm import sessionmaker

# Criando a Sessão com o Banco de Dados
Session = sessionmaker(bind=engineDb())
session = Session()

# Brasil.io Dados Nascionais
get_brasilapi.test(session)
# Brasil.io Dados Cartório
#get_cartorio.insertData(session)

session.Close()
