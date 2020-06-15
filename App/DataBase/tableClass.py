from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from .engineCreator import engineDb

engine = engineDb()
Base = declarative_base()

class Brasilapi_nacional(Base):
    __tablename__ = 'Brasil_api_base_nacional'

    id = Column(Integer, primary_key=True)
    uid = Column(String)
    uf = Column(String)
    state = Column(String)
    cases = Column(String)
    deaths = Column(String)
    suspects = Column(String)
    refuses = Column(String)
    datetime = Column(Date)
    insert_date = Column(Date)

class Brasilapi_mundo(Base):
    __tablename__ = 'Brasil_api_base_mundo'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    cases = Column(String)
    confirmed = Column(String)
    deaths = Column(String)
    recovered = Column(String)
    updated_at = Column(Date)
    insert_date = Column(Date)

def Brasil_io_nacional():
    
    dbFormat = {
    "date": Date(),
    "city_ibge_code": Integer(),
    "estimated_population_2019": Integer()
    }

    return dbFormat

def Brasil_io_cartorio():

    dbFormat = {
    "date": Date(),
    "deaths_covid19": Integer(),
    "deaths_indeterminate_2019": Integer(),
    "deaths_indeterminate_2020": Integer(),
    "estimated_population_2019": Integer(),
    "deaths_others_2019": Integer(),
    "deaths_others_2020": Integer(),
    "deaths_pneumonia_2019": Integer(),
    "deaths_pneumonia_2020": Integer(),
    "deaths_respiratory_failure_2019": Integer(),
    "deaths_respiratory_failure_2020": Integer(),
    "deaths_sars_2019": Integer(),
    "deaths_sars_2020": Integer(),
    "deaths_septicemia_2019": Integer(),
    "deaths_septicemia_2020": Integer(),
    "new_deaths_covid19": Integer(),
    "new_deaths_indeterminate_2019": Integer(),
    "new_deaths_indeterminate_2020": Integer(),
    "new_deaths_others_2019": Integer(),
    "new_deaths_others_2020": Integer(),
    "new_deaths_pneumonia_2019": Integer(),
    "new_deaths_pneumonia_2020": Integer(),
    "new_deaths_respiratory_failure_2019": Integer(),
    "new_deaths_respiratory_failure_2020": Integer(),
    "new_deaths_sars_2019": Integer(),
    "new_deaths_sars_2020": Integer(),
    "new_deaths_septicemia_2019": Integer(),
    "new_deaths_septicemia_2020": Integer()
    }

    return dbFormat

def Hdx_mundo():

    dbFormat = {
    "Date": Date()
    }

    return dbFormat

def WCota_nacional():

    dbFormat = {         
    "date": Date()
    }

    return dbFormat

def WCota_leitos():

    dbFormat = {
    "leitosOcupados": Integer(),
    "quantidadeLeitos": Integer(),
    "totalOcupacao": Float(),
    "ultimaAtualizacao": Date()
    }

    return dbFormat

def WCota_suspeitos():

    dbFormat = {
    "Casos": Integer(),
    "Suspeitos": Integer(),
    "Recuperados": Integer(),
    "Obitos": Integer(),
    "Testes": Integer(),
    "novosCasos": Integer(),
    "novosObitos": Integer()
    }

    return dbFormat

def SESA_parana():

    dbFormat = {
    "CONFIRMADOS": Integer(),
    "OBITOS": Integer(),
    "DATA": Date()
    }

    return dbFormat

def Insumos():
    
    dbFormat = {
    "Vacinas_Distribuidas_Influenza": Integer(),
    "Vacinas_Aplicadas_Influenza": Integer(),
    "Cloroquina_Comprimido": Integer(),
    "Oseltamivir_Capsulas": Integer(),
    "Teste_PCR": Integer(),
    "Leitos_Locados": Integer(),
    "Leitos_UTI_Adulto": Integer(),
    "Respiradores_Distribuidos": Integer(),
    "UTI_Adulto_SUS": Integer(),
    "UTI_Adulto_nSUS": Integer(),
    "Leitos_UTI_Habilitado": Integer(),
    "MaisMedicos": Integer()
    }

    return dbFormat

def tableCreator():

    Base.metadata.create_all(engine)

    return ''
