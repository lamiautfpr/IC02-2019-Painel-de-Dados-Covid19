from Scripts.Brasil_io import get_brasil, get_cartorio
from DataBase.engineCreator import engineDb
from sqlalchemy.orm import sessionmaker

# Criando a Sessão com o Banco de Dados
Session = sessionmaker(bind=engineDb())
session = Session()

# Brasil.io Dados Nascionais
get_brasil.insertData(session)
# Brasil.io Dados Cartório
# get_cartorio.insertData(session)

session.Close()
