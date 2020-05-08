from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint
from sqlalchemy import ForeignKey, Date, Time, BigInteger
from engineCreator import engineDb

engine = engineDb()
Base = declarative_base()


class Brasilio_nacional(Base):
    __tablename__ = 'Brasil_io_base_nacional'

    id = Column(Integer, primary_key=True)
    city = Column(String(64)),
    city_ibge = Column(String(127)),
    confirmed = Column(Integer),
    confirmed_100k = Column(float),
    date = Column(String(10)),
    death_rate = Column(float),
    deaths = Column(Integer),
    population_2019 = Column(Integer),
    is_last = Column(Boolean),
    place_type = Column(String(5)),
    state = Column(String(2)),
    insert_date = Column(Date)


class Brasilio_cartorio(Base):
    __tablename__ = 'Brasil_io_base_cartorio'

    id = Column(Integer, primary_key=True)
    date = Column(String(10)),
    state = Column(String(2)),
    epidemiological_week_2019 = Column(Integer),
    epidemiological_week_2020 = Column(Integer),
    deaths_total_2019 = Column(Integer),
    deaths_total_2020 = Column(Integer),
    new_deaths_total_2019 = Column(Integer),
    deaths_covid19 = Column(Integer),
    new_deaths_total_2020 = Column(Integer),
    deaths_indeterminate_2019 = Column(Integer),
    deaths_indeterminate_2020 = Column(Integer),
    deaths_others_2019 = Column(Integer),
    deaths_others_2020 = Column(Integer),
    deaths_pneumonia_2019 = Column(Integer),
    deaths_pneumonia_2020 = Column(Integer),
    deaths_respiratory_failure_2019 = Column(Integer),
    deaths_respiratory_failure_2020 = Column(Integer),
    deaths_sars_2019 = Column(Integer),
    deaths_sars_2020 = Column(Integer),
    deaths_septicemia_2019 = Column(Integer),
    deaths_septicemia_2020 = Column(Integer),
    new_deaths_covid19 = Column(Integer),
    new_deaths_indeterminate_2019 = Column(Integer),
    new_deaths_indeterminate_2020 = Column(Integer),
    new_deaths_others_2019 = Column(Integer),
    new_deaths_others_2020 = Column(Integer),
    new_deaths_pneumonia_2019 = Column(Integer),
    new_deaths_pneumonia_2020 = Column(Integer),
    new_deaths_respiratory_failure_2019 = Column(Integer),
    new_deaths_respiratory_failure_2020 = Column(Integer),
    new_deaths_sars_2019 = Column(Integer),
    new_deaths_sars_2020 = Column(Integer),
    new_deaths_septicemia_2019 = Column(Integer),
    new_deaths_septicemia_2020 = Column(Integer)

class Brasilapi_nacional(Base):
    __tablename__ = 'Brasil_api_base_nacional'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer),
    uf = Column(String(64)),
    state = Column(String(2)),
    cases = Column(Integer),
    deaths = Column(Integer),
    suspects = Column(Integer),
    refuses = Column(Integer),
    datetime = Column(String(25)),
    insert_date = Column(Date)


class Brasilapi_mundo(Base):
    __tablename__ = 'Brasil_api_base_mundo'

    id = Column(Integer, primary_key=True)
    country = Column(String(64)),
    cases = Column(Integer),
    confirmed = Column(Integer),
    deaths = Column(Integer),
    recovered = Column(Integer),
    updated_at = Column(String(25)),
    insert_date = Column(Date)
