from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint
from sqlalchemy import ForeignKey, Date, Time, BigInteger
from engineCreator import engineDb

engine = engineDb()
Base = declarative_base()


class Brasil_io(Base):
    __tablename__ = 'Brasil_io_base'

    id = Column(Integer, primary_key=True)


class Brasil_api(Base):
    __tablename__ = 'Brasil_api_base'

    id = Column(Integer, primary_key=True)
