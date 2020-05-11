from Scripts.functions import now
from sqlalchemy import update, text
from . import tableClass

now = now()


class Insert():

    def __init__(self, session):
        self.session = session

    def Brasilio_nacional(self, data):

        table = tableClass.Brasilio_nacional

        insert = table(
            city=data[0],
            city_ibge=data[1],
            confirmed=data[2],
            confirmed_100k=data[3],
            date=data[4],
            death_rate=data[5],
            deaths=data[6],
            population_2019=data[7],
            is_last=data[8],
            place_type=data[9],
            state=data[10],
            insert_date=now
        )

        self.session.add(insert)
        self.session.commit()

        return ''

    def Brasilio_cartorio(self, data):

        table = tableClass.Brasilio_cartorio

        insert = table(
            city=data[0]
        )

        self.session.add(insert)
        self.session.commit()

        return ''


class Select():

    def __init__(self, session):
        self.session = session

    def LastDate(self, field, table):
        query = text("SELECT TOP 1({}) FROM {}".format(field, table))
        result = self.session.execute(query)

        for row in result:
            last = row[0]
        return last
