!#/bin/bash

wget https://www.gstatic.com/covid19/mobility/Region_Mobility_Report_CSVs.zip -O /var/projetos-lamia/2019/IC02-2019-Painel-de-Dados-Covid19/src/Region_Mobility_Report_CSVs.zip

chmod a+x /var/projetos-lamia/2019/IC02-2019-Painel-de-Dados-Covid19/src/Region_Mobility_Report_CSVs.zip

unzip /var/projetos-lamia/2019/IC02-2019-Painel-de-Dados-Covid19/src/Region_Mobility_Report_CSVs.zip -d /var/projetos-lamia/2019/IC02-2019-Painel-de-Dados-Covid19/src/ *_BR*

rm /var/projetos-lamia/2019/IC02-2019-Painel-de-Dados-Covid19/src/Region_Mobility_Report_CSVs.zip

python3	/var/projetos-lamia/2019/IC02-2019-Painel-de-Dados-Covid19/src/get_mob.py

rm /var/projetos-lamia/2019/IC02-2019-Painel-de-Dados-Covid19/src/*.csv
