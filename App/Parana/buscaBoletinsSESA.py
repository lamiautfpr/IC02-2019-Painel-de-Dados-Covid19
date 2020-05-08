from datetime import timedelta, datetime, date
import pandas as pd
import numpy as np
import unicodedata
import itertools
import re

initial_date = 0
dataset = 0
date_control = True

def cleaner(temp_dataset):
    columns = [temp_dataset.columns[1:len(temp_dataset.columns)]]

    if 'Unnamed' in str(columns):
        newColumns = temp_dataset.loc[0].tolist()
        temp_dataset.columns = newColumns

    if 'IBGE' in str(newColumns):
            temp_dataset = temp_dataset.drop(['IBGE'], axis=1)

    if len(temp_dataset.columns) > 7:
        over_columns = [temp_dataset.columns[7:len(temp_dataset.columns)]]
        temp_dataset.drop(columns[0], inplace=True, axis=1)

    i=0
    while len(temp_dataset.columns) < 7:
        temp_dataset['NaN{}'.format(i)] = np.nan
        i+=1

    head = [
        "REGIONAL DE SAUDE",
        "MUNICIPIO",
        "CONFIRMADOS",
        "OBITOS",
        "DESCARTADOS",
        "EM INVESTIGACAO",
        "TOTAL",
        "DATA"
    ]    
    
    arr = temp_dataset[1:].values

    dataset = pd.DataFrame(data=arr,
                        columns=head)

    return dataset

def today():
    today = datetime.now()
    today = today.strftime('%d/%m/%Y')

    return today


def getData(date, url_data, date_control):

    if date_control is True:
        url = ("http://www.saude.pr.gov.br/arquivos/File/CORONA_{}.csv"
               ).format(url_data)
    else:
        url = ("http://www.saude.pr.gov.br/arquivos/File/INFORME_EPIDEMIOLOGICO_{}.csv"
               ).format(url_data)
    dataset = pd.read_csv(
        url, sep=',|;', encoding='ISO-8859-1', error_bad_lines=False, engine='python')

    cleaner(dataset, url_data)

    dataset["Data"] = date
    date = datetime.strptime(date, '%d/%m/%Y')
    datevar = datetime(2020, 4, 27)
    if date > datevar:
        pass
    else:
        empty_cols = [
            col for col in dataset.columns if dataset[col].isnull().all()]

        dataset.drop(empty_cols,
                     axis=1,
                     inplace=True)

    return(dataset)


def datasetConstructor(dataset, date_control):

    if date_control is True:
        dataset = dataset[2:]
    else:
        dataset = dataset[1:]

    dataset.columns = [
        "REGIONAL DE SAUDE",
        "MUNICIPIO",
        "CONFIRMADOS",
        "OBITOS",
        "DESCARTADOS",
        "EM INVESTIGACAO",
        "TOTAL",
        "DATA"
    ]

    return dataset


def getDate(d_date, date_control):

    if d_date == 0:
        d_date = datetime(2020, 4, 1)
    else:
        d_date = datetime.strptime(d_date, '%d/%m/%Y')
        d_date = d_date + timedelta(days=1)

    d_date = d_date.strftime('%d/%m/%Y')
    if date_control is True:
        url_date = d_date.replace('/', '')
    else:
        url_date = d_date.replace('/', '_')
    listdate = [d_date, url_date]

    return(listdate)


def main(date, date_control, dataset):

    while date[0] != today():

        temp_dataset = getData(date[0], date[1], date_control)
        dataframe = datasetConstructor(temp_dataset, date_control)
        if dataset is not 0:
            dataset = pd.concat([dataset, dataframe])
        else:
            dataset = dataframe
        if date[0] == '17/04/2020':
            date_control = False

        date = getDate(date[0], date_control)

    return dataset


date = getDate(initial_date, date_control)
dataset = main(date, date_control, dataset)
