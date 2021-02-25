from .engine_creator import engine_db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float


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


def WCota_vacinas():

    db_format = {
        "Data": Date(),
        "Estado": String(),
        "Suspeitos": Integer(),
        "Testes": Integer(),
        "Testes_100k": Float(),
        "Vacinados": Integer(),
        "Vacinados_100k": Float(),
        "Segunda_Dose": Integer(),
        "Segunda_Dose_100k": Float()
    }

    return db_format


def Brasil_io_nacional():
    db_format = {
    "date": Date(),
    "city_ibge_code": Integer(),
    "estimated_population_2019": Integer()
    }
    return db_format


def Brasil_io_cartorio():
    db_format = {
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
    return db_format

def get_sesa_vacinas():

    db_format = {
        'Regional': String(),
        'Municipio': String(),
        'Trabalhadores': Integer(),
        '1-Dose': Integer(),
        '2-Dose': Integer(),
        'Numero_Doses': Integer(),
        'Numero_Arredondado': Integer(),
        'Data_Insercao': Date()
    }
    
    return db_format