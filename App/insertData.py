from Scripts.Brasil_io import get_brasilio, get_cartorio
from Scripts.Brasil_api import get_brasilapi, get_mundo
from Scripts.HDX import get_mundo_hdx
from Scripts.WCota import get_wcota_nacional, get_wcota_leitos, get_wcota_suspects
from Scripts.SRAG_Covid_Brasil import get_srag
from Scripts.SESA import get_base_parana, get_base_pdf
from Scripts.SESA_PDF import get_sesa_pdf_leitos
from Scripts.Insumos import get_base_insumos
from Scripts.PR_Regioes import get_regioes
from DataBase.engineCreator import engineDb
from sqlalchemy.orm import sessionmaker
from contextlib import suppress

def insertAll():
    Session = sessionmaker(bind=engineDb())
    session = Session()

    # with suppress(Exception):
    #     get_brasilio.insertData(session)
    #     print("-> Dados inseridos com sucesso!")
    
    # with suppress(Exception):
    #     get_cartorio.insertData(session)
    #     print("-> Dados inseridos com sucesso!")
    
    with suppress(Exception):
        get_brasilapi.insertData(session)
        print("-> Dados inseridos com sucesso!")
    
    with suppress(Exception):
        get_mundo.insertData(session)
        print("-> Dados inseridos com sucesso!")
    
    with suppress(Exception):
        get_mundo_hdx.insertData(session)
        print("-> Dados inseridos com sucesso!")
    
    with suppress(Exception):
        get_wcota_nacional.insertData(session)
        print("-> Dados inseridos com sucesso!")
    
    with suppress(Exception):
        get_wcota_leitos.insertData(session)
        print("-> Dados inseridos com sucesso!")
    
    with suppress(Exception):
        get_wcota_suspects.insertData(session)
        print("-> Dados inseridos com sucesso!")

    with suppress(Exception):
        get_srag.insertData(session)
        print("-> Dados inseridos com sucesso!")

    # with suppress(Exception):
    #     get_base_parana.insertData(session)
    #     print("-> Dados inseridos com sucesso!")

    with suppress(Exception):
        get_base_pdf.insertData(session)
        print("-> Dados inseridos com sucesso!")

    with suppress(Exception):
        get_base_insumos.insertData(session)
        print("-> Dados inseridos com sucesso!")

    with suppress(Exception):
        get_sesa_pdf_leitos.insertData(session)
        print("-> Dados inseridos com sucesso!")

    session.close()
    return

insertAll()