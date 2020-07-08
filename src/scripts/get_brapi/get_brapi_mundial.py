import pandas as pd
from database import table_class
from scripts.functions import now, get_api

def catcher():
    url = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil/20200318'
    content = get_api(url)

    df = pd.DataFrame.from_dict(content)
    print(df)
    return
