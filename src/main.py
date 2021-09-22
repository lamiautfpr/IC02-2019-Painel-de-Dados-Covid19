from sqlalchemy.orm import sessionmaker
from contextlib import suppress
from database.engine_creator import engine_db
from scripts.get_hdx import get_hdx_mundial
from scripts.get_sesa import get_sesa_sheets, get_sesa_leitos, get_sesa_pr, get_sesa_time_pr, get_sesa_vacinas
from scripts.get_wcota import get_wcota_leitos, get_wcota_nacional, get_wcota_suspeitos, get_wcota_vacinas
from scripts.get_brio import get_brio_nacional, get_brio_cartorio
from scripts.get_brapi import get_brapi_nacional, get_brapi_mundial

def insert_all():
    Session = sessionmaker(bind=engine_db())
    session = Session()
    
    # get_sesa_time_pr.insert(session)
    # get_sesa_vacinas.insert(session)
    # get_wcota_vacinas.insert(session)
    get_wcota_nacional.insert(session)
   
    # Get_HDX_Mundial
    # with suppress(Exception):
    #     get_hdx_mundial.insert(session)

    # # Get_SESA_Sheets
    # with suppress(Exception):
    #     get_sesa_sheets.insert(session)


    # # Get_SESA_PDF
    # with suppress(Exception):
    # get_sesa_leitos.insert(session)


    # # Get_SESA_PR
    # with suppress(Exception):
    # get_sesa_pr.insert(session)


    # # Get_WCota_Leitos
    # with suppress(Exception):
    #     get_wcota_leitos.insert(session)


    # # Get_WCota_Nacional
    # with suppress(Exception):
    #     get_wcota_nacional.insert(session)


    # # Get_WCota_Suspeitos
    # with suppress(Exception):
    #     get_wcota_suspeitos.insert(session)


    # # Get_BRio_Nacional
    # with suppress(Exception):
    #     get_brio_nacional.insert(session)


    # # Get_BRio_Cartorio
    # with suppress(Exception):
    #     get_brio_cartorio.insert(session)


    # # Get_BRApi_Nacional
    # with suppress(Exception):
    #     get_brapi_nacional.insert(session)


    # # Get_BRApi_Mundial
    # with suppress(Exception):
    #     get_brapi_mundial.insert(session)


    session.close()
    return


if __name__ == '__main__':
    insert_all()
