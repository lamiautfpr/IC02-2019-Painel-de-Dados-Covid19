from DataBase import tableClass
import pandas as pd

def cleaner(dataset, word):
    
    dataset.rename(columns={'Value': '{}'.format(word.capitalize())}, inplace=True)

    dataset = dataset[1:]

    return dataset

def catcher():

    data = ["confirmed", "deaths", "recovered"]

    dataset = pd.DataFrame()

    for word in data:
        url = ("https://data.humdata.org/hxlproxy/data/download/time_series_covid19_{}_global_narrow.csv?dest=data_edit&filter01=merge&merge-url01=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D1326629740%26single%3Dtrue%26output%3Dcsv&merge-keys01=%23country%2Bname&merge-tags01=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&filter02=merge&merge-url02=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vTglKQRXpkKSErDiWG6ycqEth32MY0reMuVGhaslImLjfuLU0EUgyyu2e-3vKDArjqGX7dXEBV8FJ4f%2Fpub%3Fgid%3D398158223%26single%3Dtrue%26output%3Dcsv&merge-keys02=%23adm1%2Bname&merge-tags02=%23country%2Bcode%2C%23region%2Bmain%2Bcode%2C%23region%2Bsub%2Bcode%2C%23region%2Bintermediate%2Bcode&merge-replace02=on&merge-overwrite02=on&filter03=explode&explode-header-att03=date&explode-value-att03=value&filter04=rename&rename-oldtag04=%23affected%2Bdate&rename-newtag04=%23date&rename-header04=Date&filter05=rename&rename-oldtag05=%23affected%2Bvalue&rename-newtag05=%23affected%2Binfected%2Bvalue%2Bnum&rename-header05=Value&filter06=clean&clean-date-tags06=%23date&filter07=sort&sort-tags07=%23date&sort-reverse07=on&filter08=sort&sort-tags08=%23country%2Bname%2C%23adm1%2Bname&tagger-match-all=on&tagger-default-tag=%23affected%2Blabel&tagger-01-header=province%2Fstate&tagger-01-tag=%23adm1%2Bname&tagger-02-header=country%2Fregion&tagger-02-tag=%23country%2Bname&tagger-03-header=lat&tagger-03-tag=%23geo%2Blat&tagger-04-header=long&tagger-04-tag=%23geo%2Blon&header-row=1&url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_{}_global.csv".format(word, word))
        if word == "confirmed":
            temp_dataset = pd.read_csv(url, encoding='ISO-8859-1', engine='python', error_bad_lines=False, usecols=["Country/Region", "Date", "Value"])    
        else:
            temp_dataset = pd.read_csv(url, encoding='ISO-8859-1', engine='python', error_bad_lines=False, usecols=["Value"])

        temp_dataset = cleaner(temp_dataset, word)
        
        dataset = pd.concat([dataset, temp_dataset], axis=1)
        
        dataset = dataset.sort_values(by='Date', ascending=False)

        dataset.reset_index(drop=True, inplace=True)

    return dataset

def insertData(session):

    dbFormat = tableClass.Hdx_mundo()

    dataset = catcher()
    
    dataset.to_sql('HDX_base_mundo', con=session.get_bind(), index_label='id', if_exists='replace', method='multi', dtype=dbFormat)

    return ''