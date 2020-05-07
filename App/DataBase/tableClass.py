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


class Brasilapi_nacional(Base):
    __tablename__ = 'Brasil_api_base_nacional'

    id = Column(Integer, primary_key=True)
    uid = Column(String),
    uf = Column(String),
    state = Column(String),
    cases = Column(String),
    deaths = Column(String),
    suspects = Column(String),
    refuses = Column(String),
    datetime = Column(String),
    insert_date = Column(Date)


class Brasilapi_mundo(Base):
    __tablename__ = 'Brasil_api_base_mundo'

    id = Column(Integer, primary_key=True)
    country = Column(String),
    cases = Column(String),
    confirmed = Column(String),
    deaths = Column(String),
    recovered = Column(String),
    updated_at = Column(String),
    insert_date = Column(Date)
