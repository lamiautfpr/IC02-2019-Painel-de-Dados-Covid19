from sqlalchemy.orm import sessionmaker
from contextlib import suppress
from database.engine_creator import engine_db
from scripts.get_hdx import get_hdx_mundo
from scripts.get_sesa import get_sesa_sheets
from scripts.get_wcota import get_wcota_leitos, get_wcota_nacional, get_wcota_suspeitos
from scripts.get_brio import get_brio_nacional, get_brio_cartorio


def insert_all():
    Session = sessionmaker(bind=engine_db())
    session = Session()

    # #Get_HDX_Mundo
    # with suppress(Exception):
    #     get_hdx_mundo.insert(session)

    # #Get_SESA_Sheets
    # with suppress(Exception):
    #     get_sesa_sheets.insert(session)

    # #Get_WCota_Leitos
    # with suppress(Exception):
    #     get_wcota_leitos.insert(session)

    # #Get_WCota_Nacional
    # with suppress(Exception):
    #     get_wcota_nacional.insert(session)

    # #Get_WCota_Suspeitos
    # with suppress(Exception):
    #     get_wcota_suspeitos.insert(session)

    # with suppress(Exception):
    get_brio_nacional.insert(session)

    with suppress(Exception):
        get_brio_cartorio.insert(session)

    session.close()
    return

insert_all()