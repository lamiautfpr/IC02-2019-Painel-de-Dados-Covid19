import pandas as pd

url = ("http://www.saude.pr.gov.br/arquivos/File/INFORME_EPIDEMIOLOGICO_03_05_2020.csv")
dataset = pd.read_csv(url, sep=",", encoding='ISO-8859-1')
header = dataset.iloc[0]
dataset = dataset[2:]
dataset.columns = header
print(dataset)
