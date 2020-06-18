from Scripts.Brasil_io import get_brasilio, get_cartorio
from Scripts.Brasil_api import get_brasilapi, get_mundo
from Scripts.HDX import get_mundo_hdx
from Scripts.WCota import get_wcota_nacional, get_wcota_leitos, get_wcota_suspects
from Scripts.SRAG_Covid_Brasil import get_srag
from Scripts.SESA import get_base_parana, get_base_pdf
from Scripts.Insumos import get_base_insumos
from Scripts.PR_Regioes import get_regioes
from DataBase.engineCreator import engineDb
from sqlalchemy.orm import sessionmaker

def insertAll():
    
    Session = sessionmaker(bind=engineDb())
    session = Session()

    try:
        get_brasilio.insertData(session)
        print("Os dados da Brasil.io Base Nacional foram inseridos corretamente.")
    except:
        print("Os dados da Brasil.io Base Nacional não foram inseridos.")
        pass

    try:
        get_cartorio.insertData(session)
        print("Os dados Brasil.io Base Cartório inseridos corretamente.")
    except:
        print("Os dados da Brasil.io Base Cartório não foram inseridos.")
        pass

    try:
        get_brasilapi.insertData(session)
        print("Os dados Brasil.api Base Nacional foram inseridos corretamente.")
    except:
        print("Os dados da Brasil.api Base Nacional não foram inseridos.")
        pass

    try:
        get_mundo.insertData(session)
        print("Os dados Brasil.api Base Mundo foram inseridos corretamente.")
    except:
        print("Os dados da Brasil.api Base Mundo não foram inseridos.")
        pass

    try:
        get_mundo_hdx.insertData(session)
        print("Os dados da HDX Base Mundo foram inseridos corretamente.")
    except:
        print("Os dados da HDX Base Mundo não foram inseridos.")
        pass

    try:
        get_wcota_nacional.insertData(session)
        print("Os dados da WCota Base Nacionais foram inseridos corretamente.")
    except:
        print("Os dados da WCota Base Nacionais não foram inseridos.")
        pass

    try:
        get_wcota_leitos.insertData(session)
        print("Os dados da WCota Base Leitos foram inseridos corretamente.")
    except:
        print("Os dados da WCota Base Leitos não foram inseridos.")
        pass

    try:
        get_wcota_suspects.insertData(session)
        print("Os dados da WCota Base Suspeitos foram inseridos corretamente.")
    except:
        print("Os dados da WCota Base Suspeitos não foram inseridos.")
        pass

    try:
        get_srag.insertData(session)
        print("Os dados da SRAG Base Nacionais foram inseridos corretamente.")
    except:
        print("Os dados da SRAG Base Nacionais não foram inseridos.")
        pass

    try:
        get_base_parana.insertData(session)
        print("Os dados da SESA Base Paraná foram inseridos corretamente.")
    except:
        print("Os dados da SESA Base Paraná não foram inseridos.")
        pass

    try:
        get_base_pdf.insertData(session)
        print("Os dados da SESA Base PDF foram inseridos corretamente.")
    except:
        print("Os dados da SESA Base PDF não foram inseridos.")
        pass

    try:
        get_base_insumos.insertData(session)
        print("Os dados da Insumos Base Nacional foram inseridos corretamente.")
    except:
        print("Os dados da Insumos Base Nacional não foram inseridos.")
        pass

    return

insertAll()