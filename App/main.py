from Scripts.Brasil_io import get_brasilio, get_cartorio
from Scripts.Brasil_api import get_brasilapi, get_mundo
from DataBase.engineCreator import engineDb
from sqlalchemy.orm import sessionmaker

# Criando a Sessão com o Banco de Dados
Session = sessionmaker(bind=engineDb())
session = Session()

# Brasil.io Dados Nascionais
get_brasil.insertData(session)
# Brasil.io Dados Cartório
get_cartorio.insertData(session)

# Brasil.api Dados Nacionais
get_brasilapi.insertData(session)
# Brasil.api Dados Mundiais
get_mundo.insertData(session)

session.Close()
