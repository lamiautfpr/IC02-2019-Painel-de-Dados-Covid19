from . import table_class
from sqlalchemy import update, text
from scripts.functions import now, format_date

class Insert():


    def __init__(self, session):
        self.session = session


    def Brasilapi_mundo(self, data):
        table = table_class.Brasilapi_mundo

        insert = table(
            country=data[0],
            cases=data[1],
            confirmed=data[2],
            deaths=data[3],
            recovered=data[4],
            updated_at=format_date(1, data[5]),
            insert_date=now()
        )

        self.session.add(insert)
        self.session.commit()
        return


    def Brasilapi_nacional(self, data):
        table = table_class.Brasilapi_nacional

        insert = table(
            uid=data[0],
            uf=data[1],
            state=data[2],
            cases=data[3],
            deaths=data[4],
            suspects=data[5],
            refuses=data[6],
            datetime=data[7],
            insert_date=now()
        )

        self.session.add(insert)
        self.session.commit()
        return

class Select():


    def __init__(self, session):
        self.session = session


    def Date(self, field, table):
        query = text("SELECT MAX({}) FROM {}".format(field, table))
        result = self.session.execute(query)

        for row in result:
            last = row[0]

        return last