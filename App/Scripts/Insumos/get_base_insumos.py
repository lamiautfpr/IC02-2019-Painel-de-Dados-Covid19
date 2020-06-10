from Scripts.functions import now        
from urllib.request import Request, urlopen
from DataBase import tableClass
import pandas as pd

def cleaner(temp_dataset):
    
    arr = temp_dataset[0:].values

    head = [
        "UF",
        "Vacinas_Distribuidas_Influenza",
        "Vacinas_Aplicadas_Influenza",
        "Mascara_Cirurgica",
        "Mascara_N95",
        "alcoolGel/L",
        "Avental",
        "Teste_Rapido",
        "Luva",
        "Oculos_protetorFacial",
        "Touca/Sapatilha",
        "Cloroquina_Comprimido",
        "Oseltamivir_Capsulas",
        "Teste_PCR",
        "Leitos_Locados",
        "Leitos_UTI_Adulto",
        "Respiradores_Distribuidos",
        "UTI_Adulto_SUS",
        "UTI_Adulto_nSUS",
        "Leitos_UTI_Habilitado",
        "MaisMedicos",
    ]

    dataset = pd.DataFrame(data=arr,
                          columns=head)

    return dataset

def catcher():

    url = ("https://covid-insumos.saude.gov.br/paineis/insumos/lista_csv_painel.php?output=csv")
    dataset = pd.read_csv(url, encoding='utf-8', engine='python', error_bad_lines=False, sep=';')
    
    dataset = cleaner(dataset)

    dataset.insert(len(dataset.columns), "insert_date", now())

    return dataset

def insertData(session):

    print("Coletando e inserindo dados para Insumos_base_nacional...")

    dbFormat = tableClass.Insumos()

    dataset = catcher()
    
    dataset.to_sql('Insumos_base_nacional', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', chunksize=50000, dtype=dbFormat)
    
    return ''
