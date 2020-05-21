from DataBase.engineCreator import engineDb
from Scripts.Brasil_io import get_brasil, get_cartorio
from Scripts import get_insumos 
from sqlalchemy.orm import sessionmaker

# Criando a Sessão com o Banco de Dados
Session = sessionmaker(bind=engineDb())
session = Session()

# BR.io -------------------
# Brasil.io Dados Nacionais
get_brasil.insertData(session)
# Brasil.io Dados Cartório
#get_cartorio.insertData(session)


# BR.api -------------------
# Brasil.apiNacional
#get_brasilapi.insertData(session)
# Brasil.apiMundial
#get_mundo.insertData(session)

#saude.gov.br -------------------
#get_insumos.insertData(session)