<h1 align="center">
  <br>
  <a href="https://www.lamia.sh.utfpr.edu.br/">
    <img src="https://user-images.githubusercontent.com/26206052/86039037-3dfa0b80-ba18-11ea-9ab3-7e0696b505af.png" alt="LAMIA - Laboratório de                  Aprendizagem de Máquina e Imagens Aplicados à Indústria" width="400"></a>
<br> <br>
Painel de Dados Coronavírus (COVID-19) - Paraná
<h4 align="center"><a href="https://bit.ly/paineldadoscovid19" target="_blank">Informe Epidemiológico Inteligente</a></h4>
</h1>

<p align="center">
  <a href="https://www.lamia.sh.utfpr.edu.br/">
    <img src="https://img.shields.io/badge/Follow-Lab%20Page-blue" alt="Lab">
  <a href="https://bit.ly/paineldadoscovid19">
    <img src="https://img.shields.io/badge/Application-PowerBI-black" alt="Application">
  <a href="https://github.com/lamia-utfpr/IC02-2019-Painel-de-Dados-Covid19/blob/Produ%C3%A7%C3%A3o/LICENSE">
    <img src="https://img.shields.io/github/license/lamia-utfpr/IC02-2019-Painel-de-Dados-Covid19" alt="License">
  <a href="https://github.com/lamia-utfpr/IC02-2019-Painel-de-Dados-Covid19">
    <img src="https://img.shields.io/badge/Build-2.0-green" alt="Build 2.0">
   </a></a></a></a>
</p>

<p align="center">
<b>Equipe:</b>  
<br>
Thiago Naves <a href="https://github.com/tfnaves" target="_blank"> (Naves, T. F.)</a> - Coordenador  <br>
Arlete Beuren <a href="https://github.com/arleteb" target="_blank"> (Beuren, A. T.)</a> - Orientadora  <br>
Anderson Brilhador <a href="https://github.com/Brilhador" target="_blank">(Brilhador, A.)</a> - Orientador  <br>
Nathalia de Oliveira <a href="https://github.com/nathmota" target="_blank">(Oliveira, N. V. M.)</a> - Membro Líder  <br>
Jece Neto <a href="https://github.com/XavierJece" target="_blank">(Neto, J. X. P.)</a> - Membro  <br>
Guilherme Yoshida <a href="https://github.com/guiyshd" target="_blank">(Yoshida, G.)</a> - 	Membro  <br>
Hugo de Freitas <a href="https://github.com/HugoJFreitas" target="_blank">(Freitas, H. J. T</a>) - Membro  <br>
</p>

<p align="center">
<b>Parceiros:</b>  
<br>
Sistema Regional de Inovação do Oeste do Paraná <a href="https://sri.oesteemdesenvolvimento.com.br/" target="_blank"> (SRI Iguassu Valley )</a>   <br>
Koredata <a href="https://biopark.com.br/site/pt/blog_detalhes/nova-residente-no-biopark-atua-com-solues-em-inteligncia-de-mercado" target="_blank"> (Koredata)</a>  <br>
</p>


<p align="center">  
<b>Grupo</b>: <a href="https://www.lamia.sh.utfpr.edu.br/" target="_blank">LAMIA - Laboratório de Aprendizado de Máquina e Imagens Aplicados à Indústria </a> <br>
<b>Email</b>: <a href="mailto:lamia-sh@utfpr.edu.br" target="_blank">lamia-sh@utfpr.edu.br</a> <br>
<b>Organização</b>: <a href="http://portal.utfpr.edu.br" target="_blank">Universidade Tecnológica Federal do Paraná</a> <a href="http://www.utfpr.edu.br/campus/santahelena" target="_blank"> - Campus Santa Helena</a> <br>
</p>

<p align="center">
<br>
Status do Projeto: Em desenvolvimento :warning:
</p>

<p align="center">
  <a href="https://www.loom.com/share/078eb1ade510400ea0826053973d385e">
    <img src="https://user-images.githubusercontent.com/26206052/86052555-8c65d500-ba2d-11ea-8265-0e1acd1d521c.gif" width="900">
  </a>
</p>

___

## Resumo
O projeto utiliza das tecnologias de ciência dos dados para desenvolver uma plataforma de monitoramento e análise inteligente dos dados do Covid-19 em relação a confirmados, óbitos, tipos de óbitos, suspeitos, recuperados, leitos, dentre outros dados. A plataforma possui foco maior no estado do Paraná e faz monitoramento dos demais estados do Brasil e dos países do restante do mundo. O painel também possui a finalidade de manter as pessoas informadas acerca dos avanços do coronavírus e pode ser acessado [paineldadoscovid19](https://bit.ly/paineldadoscovid19).

O código disponível no github são dos scripts necessários para obter os dados e cadastrá-los no banco de dados, as visualizações da plataforma são desenvolvidas utilizando Microsoft Power BI.

![Painel 3](https://user-images.githubusercontent.com/26206052/86056446-d94caa00-ba33-11ea-9738-f8f5713fd5dd.png)

## Objetivos
O objetivo principal do projeto Painel Paraná Covid-19 é monitorar de forma inteligente os dados do coronavírus prioritariamente no estado do Paraná e no restante do Brasil, com dados atualizados em tempo real e com uso de algoritmos de inteligência artificial para executar predições e construir relatórios para tomadas de decisão por parte dos órgãos públicos e privados que atuam no combate do covid19.

Dentre alguns dos objetivos gerais do projeto estão.
  - Coletar dados sobre o covid-19 no âmbito estadual, nacional e mundial em tempo real formando uma base de dados conscistente e confiável
  - Construir esquemas de visualização da informação de modo que a interpretação dos dados seja simples e direta por parte do público
  - Monitorar a situação do coronavírus utilizando de algoritmos de inteligência artificial para executar predições acerca da quantidade de pessoas e recursos médicos que serão afetados nos dias subsquentes formando conhecimento relevante
  - Gerar relatórios técnicos com tomadas de decisão para auxiliar as os órgãos públicos e privados no combate ao covid-19

## Como Utilizar
Para clonar e rodar está aplicação será necessário o [Git](https://git-scm.com) e o [Python3](https://www.python.org/downloads/) instalados em sua máquina. A partir da linha de comando descrita abaixo será possível clonar este repositório.

```bash
# Clone this repository
$ git clone https://github.com/lamia-utfpr/IC02-2019-Painel-de-Dados-Covid19.git

# Go into the repository
$ cd IC02-2019-Painel-de-Dados-Covid19
```
Note: If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use the command prompt from your IDE.

Agora que você já está com o repositório clonado será necessário criar um virtual environment para armazenamento das bibliotecas presentes no requeriments. No diretório do projeto utilize as linhas de comando abaixo:

```bash
# Create virtualenv
$ virtualenv venv

# Execute virtual env
$ source venv/bin/activate
```

Com o virtual enviroment criado e sendo executa será necessário baixar as bibliotecas presentes no requeriments.txt. Para isso basta utilizar o pip3 para fazer a instalação recursiva de todas as bibliotecas presentes no arquivo de texto. Certifique-se que o shell está no diretório do requeriments. Recomenda-se a utilização da execução em super usuário utilizando sudo.

```bash
# Install all requeriments
$ sudo pip3 install -r requeriments.txt
```
Com a criação do ambiente finalizada, configure o arquivo credentials.json com as credenciais de seu banco de dados e voalá! É só rodar o arquivo main.py para inserir todas as bases em seu banco de dados. É importante lembrar que não se utilize nenhum lint do Python na compilação dos algoritmos, pois o mesmo demonstra alguns bugs para importação de packages.

As bibliotecas utilizadas no projeto estão presentes no arquivo requeriments.txt.

```bash
astroid==2.4.2
autopep8==1.5.3
certifi==2020.6.20
chardet==3.0.4
colorama==0.4.3
flake8==3.8.3
idna==2.10
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
mypy==0.782
mypy-extensions==0.4.3
numpy==1.19.0
pandas==1.0.5
psycopg2==2.8.5
pycodestyle==2.6.0
pyflakes==2.2.0
pylint==2.5.3
python-dateutil==2.8.1
pytz==2020.1
requests==2.24.0
schedule==0.6.0
six==1.15.0
SQLAlchemy==1.3.18
toml==0.10.1
typed-ast==1.4.1
typing-extensions==3.7.4.2
urllib3==1.25.9
wrapt==1.12.1
```
## Tecnologias

Painel Paraná Inteligente Covid-19 usa os seguintes algoritmos e tecnologias:

* [Regressão Logística](https://medium.com/turing-talks/turing-talks-14-modelo-de-predi%C3%A7%C3%A3o-regress%C3%A3o-log%C3%ADstica-7b70a9098e43) - executar predições
* [Regressão Linear](https://medium.com/@lucasoliveiras/regress%C3%A3o-linear-do-zero-com-python-ef74a81c4b84) - executar predições
* [Mínimos Quadrados](https://www.scielo.br/scielo.php?pid=S0100-40422007000200020&script=sci_arttext) - comparar predições geradas e efetuar ajustes
* [Árvores de Decisão](https://www.vooo.pro/insights/um-tutorial-completo-sobre-a-modelagem-baseada-em-tree-arvore-do-zero-em-r-python/) - gerar tomadas de decisão com base em condições pré-estabelecidas
* [Tabula-py](https://tabula-py.readthedocs.io/en/latest/tabula.html/) - tabula-py é um wrapper Python simples de tabula-java, que pode ler a tabelad de arquivos PDF.
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/) - O SQLAlchemy SQL Toolkit e o Object Relational Mapper são um conjunto abrangente de ferramentas para trabalhar com bancos de dados e Python.
* [Requests](https://requests.readthedocs.io/en/master/) - Utilizada para fazer requisições HTTP pelo Python.
* [Schedule](https://pypi.org/project/schedule/) - O Schedule permite executar funções Python (ou qualquer outra chamada) periodicamente em intervalos predeterminados.
* [Numpy](https://numpy.org/) - plotagens de dados e gráficos
* [Pandas](https://pandas.pydata.org/) - execução de algoritmos de predição
* [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - extração automática de dados

## Citação

Se você utliza e quer citar o projeto em sua pesquisa, por favor utilize o formato de citação abaixo:
    
    @inproceedings{LAMIA_ic02,
      title={Painel Inteligente de Dados Covid-19},
      author={Naves, T. F.; BEUREN, A. T.; BRILHADOR, A.},
      journal={IEEE Conference on Big Data},
      year={2020}
    }
