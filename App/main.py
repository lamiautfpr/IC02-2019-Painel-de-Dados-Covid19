from App.DataBase.engineCreator import engineDb
from App.Scripts.Brasil_io import get_brasil
from sqlalchemy.orm import sessionmaker

# Criando a Sessão com o Banco de Dados
Session = sessionmaker(bind=engineDb())
session = Session()

get_brasil.insertData(session)
