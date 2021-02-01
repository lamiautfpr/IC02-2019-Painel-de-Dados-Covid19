from scripts.functions import now
from database import table_class
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests
import tabula

vac_columns = [
    'Regional',
    'Municipio',
    'Trabalhadores',
    '1-Dose',
    '2-Dose',
    'Numero_Doses',
    'Numero_Arredondado'
]

def transform(dfs):
    
    dfs.info()
    
    for df in dfs:
        print(df)
        print(dfs[df])
        try:
            dfs[df] = dfs[df].str.replace(".", "").astype(int)
        except:
            pass
    
    return dfs

def cleanner(dfs):

    final_df = pd.DataFrame()

    for df in dfs:
        # print(df)
        # df.info()
        df.dropna(inplace=True)
        final_df = pd.concat([final_df, df], ignore_index=True)
    

    final_df.drop([0], inplace=True)

    final_df.columns = vac_columns

    final_df = transform(final_df)

    return final_df

def insert(session):
    
    print("Inserindo get_sesa_vacinas.")

    url = "https://www.saude.pr.gov.br/sites/default/arquivos_restritos/files/documento/2021-01/anexo_iv_quantidades_de_doses_distribuidas_por_regional_e_municipios_da_vacina_covid-19_-_astrazeneca_fiocruz_para_o_grupo_trabalhadores_de_saude_.pdf"
    
    dfs = tabula.read_pdf(url, pages="all", pandas_options={'header': None, 'dtype': str})

    # print(final_df)
    # final_df.info()

    dfs = cleanner(dfs)

    print(dfs)

    db_format = table_class.get_sesa_vacinas()
    
    dfs.to_sql("SESA_Vacinas_PR", index=False, con=session.get_bind(), if_exists='replace', method='multi',
    dtype=db_format)
    
    return 0    
