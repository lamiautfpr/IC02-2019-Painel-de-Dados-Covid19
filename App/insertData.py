# from Scripts.Brasil_io import get_brasilio, get_cartorio
from Scripts.Brasil_api import get_brasilapi, get_mundo
from Scripts.HDX import get_mundo_hdx
from Scripts.WCota import get_wcota_nacional, get_wcota_leitos, get_wcota_suspects
from Scripts.SRAG_Covid_Brasil import get_srag
from Scripts.SESA import get_base_parana, get_base_pdf
from DataBase.engineCreator import engineDb
from sqlalchemy.orm import sessionmaker

# Criando a Sessão com o Banco de Dados
Session = sessionmaker(bind=engineDb())
session = Session()

# BR.io
# Brasil.io Dados Nacionais
# get_brasil.insertData(session)
# Brasil.io Dados Cartório
# get_cartorio.insertData(session)

# BR.api
# Brasil.apiNacional
get_brasilapi.insertData(session)
# Brasil.apiMundial
get_mundo.insertData(session)

# HDX
# HDX.getMundo
get_mundo_hdx.insertData(session)

# WCota
# WCota.getNacional
get_wcota_nacional.insertData(session)
# WCota.getLeitos
get_wcota_leitos.insertData(session)
# WCota.getSuspects
get_wcota_suspects.insertData(session)

# Covid Brazil
# SRAG
get_srag.insertData(session)

# SESA Paraná
# CSV
get_base_parana.insertData(session)
# PDF
get_base_pdf.insertData(session)

session.Close()