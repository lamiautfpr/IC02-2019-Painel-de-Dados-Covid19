from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint
from sqlalchemy import ForeignKey, Date, Time, BigInteger, Float
from .engineCreator import engineDb

engine = engineDb()
Base = declarative_base()

class Brasilio_nacional(Base):
    __tablename__ = 'Brasil_io_base_nacional'

    id = Column(Integer, primary_key=True)
    city = Column(String(64))
    city_ibge = Column(String(127))
    confirmed = Column(Integer)
    confirmed_100k = Column(Float)
    date = Column(Date)
    death_rate = Column(Float)
    deaths = Column(Integer)
    population_2019 = Column(Integer)
    is_last = Column(Boolean)
    place_type = Column(String(5))
    state = Column(String(2))
    insert_date = Column(Date)


class Brasilio_cartorio(Base):
    __tablename__ = 'Brasil_io_base_cartorio'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    deaths_covid19 = Column(Integer)
    deaths_indeterminate_2019 = Column(Integer)
    deaths_indeterminate_2020 = Column(Integer)
    deaths_others_2019 = Column(Integer)
    deaths_others_2020 = Column(Integer)
    deaths_pneumonia_2019 = Column(Integer)
    deaths_pneumonia_2020 = Column(Integer)
    deaths_respiratory_failure_2019 = Column(Integer)
    deaths_respiratory_failure_2020 = Column(Integer)
    deaths_sars_2019 = Column(Integer)
    deaths_sars_2020 = Column(Integer)
    deaths_septicemia_2019 = Column(Integer)
    deaths_septicemia_2020 = Column(Integer)
    deaths_total_2019 = Column(Integer)
    deaths_total_2020 = Column(Integer)
    epidemiological_week_2019 = Column(Integer)
    epidemiological_week_2020 = Column(Integer)
    new_deaths_covid19 = Column(Integer)
    new_deaths_indeterminate_2019 = Column(Integer)
    new_deaths_indeterminate_2020 = Column(Integer)
    new_deaths_others_2019 = Column(Integer)
    new_deaths_others_2020 = Column(Integer)
    new_deaths_pneumonia_2019 = Column(Integer)
    new_deaths_pneumonia_2020 = Column(Integer)
    new_deaths_respiratory_failure_2019 = Column(Integer)
    new_deaths_respiratory_failure_2020 = Column(Integer)
    new_deaths_sars_2019 = Column(Integer)
    new_deaths_sars_2020 = Column(Integer)
    new_deaths_septicemia_2019 = Column(Integer)
    new_deaths_septicemia_2020 = Column(Integer)
    new_deaths_total_2019 = Column(Integer)
    new_deaths_total_2020 = Column(Integer)
    state = Column(String(10))
    # insert_date = Column(Date)


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
    "DESCARTADOS": Integer(),
    "INVESTIGACAO": Integer(),
    "DATA": Date()
    }

    return dbFormat


def tableCreator():

    Base.metadata.create_all(engine)

    return ''
