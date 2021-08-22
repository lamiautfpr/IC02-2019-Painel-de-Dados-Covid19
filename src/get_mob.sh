!#/bin/bash

wget https://www.gstatic.com/covid19/mobility/Region_Mobility_Report_CSVs.zip

chmod a+x Region_Mobility_Report_CSVs.zip

unzip -j Region_Mobility_Report_CSVs.zip *_BR*

rm Region_Mobility_Report_CSVs.zip

python3	/var/IC/IC02-2019-Painel-de-Dados-Covid19/src/get_mob.py

rm *.csv
