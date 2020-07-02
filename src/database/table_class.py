from sqlalchemy import Integer, Date, Float


def Hdx_mundo():
    db_format = {
        "Date": Date()
    }
    return db_format


def WCota_nacional():
    db_format = {
        "date": Date()
    }
    return db_format


def WCota_leitos():
    db_format = {
        "leitosOcupados": Integer(),
        "quantidadeLeitos": Integer(),
        "totalOcupacao": Float(),
        "ultimaAtualizacao": Date()
    }
    return db_format


def WCota_suspeitos():
    db_format = {
        "Casos": Integer(),
        "Suspeitos": Integer(),
        "Recuperados": Integer(),
        "Obitos": Integer(),
        "Testes": Integer(),
        "novosCasos": Integer(),
        "novosObitos": Integer()
    }
    return db_format
