from Scripts.functions import now, formatDate
from sqlalchemy import update, text
from . import tableClass

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
            insert_date=now()
        )

        self.session.add(insert)
        self.session.commit()

        return ''

    def Brasilio_cartorio(self, data):

        table = tableClass.Brasilio_cartorio

        # data.append(now)
        insert = table(
            date=data[0],
            deaths_covid19=data[1],
            deaths_indeterminate_2019=data[2],
            deaths_indeterminate_2020=data[3],
            deaths_others_2019=data[4],
            deaths_others_2020=data[5],
            deaths_pneumonia_2019=data[6],
            deaths_pneumonia_2020=data[7],
            deaths_respiratory_failure_2019=data[8],
            deaths_respiratory_failure_2020=data[9],
            deaths_sars_2019=data[10],
            deaths_sars_2020=data[11],
            deaths_septicemia_2019=data[12],
            deaths_septicemia_2020=data[13],
            deaths_total_2019=data[14],
            deaths_total_2020=data[15],
            epidemiological_week_2019=data[16],
            epidemiological_week_2020=data[17],
            new_deaths_covid19=data[18],
            new_deaths_indeterminate_2019=data[19],
            new_deaths_indeterminate_2020=data[20],
            new_deaths_others_2019=data[21],
            new_deaths_others_2020=data[22],
            new_deaths_pneumonia_2019=data[23],
            new_deaths_pneumonia_2020=data[24],
            new_deaths_respiratory_failure_2019=data[25],
            new_deaths_respiratory_failure_2020=data[26],
            new_deaths_sars_2019=data[27],
            new_deaths_sars_2020=data[28],
            new_deaths_septicemia_2019=data[29],
            new_deaths_septicemia_2020=data[30],
            new_deaths_total_2019=data[31],
            new_deaths_total_2020=data[32],
            state=data[33],
            # insert_date=now,

        )

        self.session.add(insert)
        self.session.commit()

        return ''

    def Brasilapi_mundo(self, data):

        table = tableClass.Brasilapi_mundo

        insert = table(
            country=data[0],
            cases=data[1],
            confirmed=data[2],
            deaths=data[3],
            recovered=data[4],
            updated_at=formatDate(3, data[5]),
            insert_date=now()
        )

        self.session.add(insert)
        self.session.commit()

        return ''

    def Brasilapi_nacional(self, data):

        table = tableClass.Brasilapi_nacional

        insert = table(
            uid=data[0],
            uf=data[1],
            state=data[2],
            cases=data[3],
            deaths=data[4],
            suspects=data[5],
            refuses=data[6],
            datetime=formatDate(3, data[7]),
            insert_date=now()
        )

        self.session.add(insert)
        self.session.commit()

        return ''

class Select():

    def __init__(self, session):
        self.session = session

    def LastDate(self, field, table):
        query = text("SELECT MAX({}) FROM {}".format(field, table))
        result = self.session.execute(query)

        for row in result:
            last = row[0]

        return last