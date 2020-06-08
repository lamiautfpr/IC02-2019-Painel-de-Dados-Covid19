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
    insert_date = Column(Date)


class Brasilapi_nacional(Base):
    __tablename__ = 'Brasil_api_base_nacional'

    id = Column(Integer, primary_key=True)
    uid = Column(String)
    uf = Column(String)
    state = Column(String)
    cases = Column(Integer)
    deaths = Column(Integer)
    suspects = Column(Integer)
    refuses = Column(Integer)
    datetime = Column(String)
    insert_date = Column(Date) 


class Brasilapi_mundo(Base):
    __tablename__ = 'Brasil_api_base_mundo'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    cases = Column(Integer)
    confirmed = Column(Integer)
    deaths = Column(Integer)
    recovered = Column(Integer)
    updated_at = Column(Date)
    insert_date = Column(Date)


class Painel_insumos(Base):
    __tablename__ = 'Painel_insumos_gov'

    id = Column(Integer, primary_key=True)
    uf = Column(String)     
    vacinas_distribuidas_influenza = Column(Integer)  
    vacinas_aplicadas_influenza = Column(Integer)  
    mascara_cirurgica = Column(Integer)  
    mascara_n95 = Column(Integer) 
    alcool_gel_L = Column(Integer) 
    avental = Column(Integer) 
    teste_rapido = Column(Integer) 
    luvas = Column(Integer) 
    oculos_e_protetor_facial = Column(Integer) 
    touca_e_sapatilha = Column(Integer) 
    cloroquina_comprimidos = Column(Integer) 
    oseltamivir_capsulas = Column(Integer) 
    teste_PCR = Column(Integer) 
    leitos_locados = Column(Integer) 
    leitos_uti_adulto = Column(Integer) 
    respiradores_distribuidos = Column(Integer) 
    uti_adulto_sus = Column(Integer) 
    uti_adulto_nao_sus = Column(Integer) 
    leitos_uti_habilitados = Column(Integer) 
    mais_medicos = Column(Integer) 
    insert_date = Column(Date)


def tableCreator():

    Base.metadata.create_all(engine)

    return ''
