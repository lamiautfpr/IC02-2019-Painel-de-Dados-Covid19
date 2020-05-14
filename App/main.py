from DataBase.engineCreator import engineDb
from Scripts.Brasil_io import get_brasil, get_cartorio
from sqlalchemy.orm import sessionmaker

# Criando a Sessão com o Banco de Dados
Session = sessionmaker(bind=engineDb())
session = Session()

# Brasil.io Dados Nacionais
get_brasil.insertData(session)
# Brasil.io Dados Cartório
get_cartorio.insertData(session)

