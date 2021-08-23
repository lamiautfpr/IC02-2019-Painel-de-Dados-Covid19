from sqlalchemy.orm import sessionmaker
from database.engine_creator import engine_db

import os
import glob
import pandas as pd
from database import table_class
from scripts.functions import now


def clean_data(dfs):

    dfs = dfs[dfs['sub_region_2'] == "Toledo"] # filtro para a cidade de toledo

    dfs.drop(columns=['country_region_code', 'country_region', 'sub_region_1', 'sub_region_2',
       'metro_area', 'iso_3166_2_code', 'census_fips_code', 'place_id'], inplace=True)

    dfs.columns = ['data', 'varejo e recreacao', 'mercearia e farmacia',
        'parques', 'estacoes de transito', 'locais de trabalho',
        'residencias']
    
    dfs.reset_index(drop=True, inplace=True)

    print(dfs)
    print(dfs.columns)

    return dfs

 
def get_data():
    
    work_dir = os.getcwd()
    files = glob.glob(os.path.join(work_dir, "*.csv"))

    print(files)
    df_list = []

    for f in files:

        df = pd.read_csv(f)
        df_list.append(df)

    dfs = pd.concat(df_list)
    # dfs.reset_index(inplace=True)
    print(dfs)
    
    dfs = clean_data(dfs)

    return dfs

def insert():
    
    print("Inserindo get_mob.")

    db_format = table_class.get_mob()
    dataset = get_data()

    Session = sessionmaker(bind=engine_db())
    session = Session()
    dataset.to_sql('get_Mobility_TL', con=session.get_bind(),
                   index=False, if_exists='replace', method='multi',
                   chunksize=50000, dtype=db_format)

    return print("get_mob inserido com sucesso!")


insert()
# gerar dataset e renomear para as seguintes colunas:

# data
# varejo e recreação
# mercearia e farmácia
# parques
# estações de trânsito
# locais de trabalho
# residências