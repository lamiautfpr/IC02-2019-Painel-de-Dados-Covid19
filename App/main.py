# from Scripts.Brasil_io import get_brasilio, get_cartorio
from Scripts.Brasil_api import get_brasilapi, get_mundo
from Scripts.HDX import get_mundo_hdx
from Scripts.WCota import get_wcota_nacional
from DataBase.engineCreator import engineDb
from sqlalchemy.orm import sessionmaker

# Criando a Sessão com o Banco de Dados
Session = sessionmaker(bind=engineDb())
session = Session()


# BR.io
# Brasil.io Dados Nacionais
#get_brasil.insertData(session)
# Brasil.io Dados Cartório
#get_cartorio.insertData(session)


# BR.api
# Brasil.apiNacional
#get_brasilapi.insertData(session)
# Brasil.apiMundial
#get_mundo.insertData(session)


# HDX
# HDX.getMundo
get_mundo_hdx.insertData(session)


# WCota
# WCota.getNacional
#get_wcota_nacional.insertData(session)

session.Close()
