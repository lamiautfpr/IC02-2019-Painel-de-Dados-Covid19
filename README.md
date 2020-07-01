<h1 align="center">
  <br>
  <a href="http://www.lamia-sh.utfpr.edu.br">
    <img src="https://user-images.githubusercontent.com/26206052/86039037-3dfa0b80-ba18-11ea-9ab3-7e0696b505af.png" alt="LAMIA - Laboratório de                  Aprendizagem de Máquina e Imagens Aplicados à Indústria" width="400"></a>
<br> <br>
  Painel Paraná Inteligente Covid-19
  <br>
</h1>

<h4 align="center">Informe Epidemiológico Inteligente.</h4>

<p align="center">
  <a href="https://lamia.sh.utfpr.edu.br">
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
Nathalia de Oliveira <a href="https://github.com/nathmota" target="_blank">(Oliveira, N. V. M.)</a> - discente líder  <br>
Guilherme Teixeira <a href="https://github.com/guiyshd" target="_blank">(Teixeira, G. Y.)</a> - 	discente  <br>
Jece Neto <a href="https://github.com/XavierJece" target="_blank">(Neto, J. X. P.)</a> - discente  <br>
Hugo de Freitas <a href="https://github.com/HugoJFreitas" target="_blank">(Freitas, H. J. T</a>) - discente  <br>
</p>

<p align="center">  
<b>Grupo</b>: <a href="https://lamia.sh.utfpr.edu.br" target="_blank">LAMIA - Laboratório de Aprendizado de Máquina e Imagens Aplicados à Indústria </a> <br>
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
  
## Resumo
O projeto utiliza das tecnologias de ciência dos dados para desenvolver uma plataforma de monitoramento e análise inteligente dos dados do Covid-19 em relação a confirmados, óbitos, tipos de óbitos, suspeitos, recuperados, leitos, dentre outros dados. A plataforma possui foco maior no estado do Paraná e faz monitoramento dos demais estados do Brasil e dos países do restante do mundo. O painel também possui a finalidade de manter as pessoas informadas acerca dos avanços do coronavírus e pode ser acessado https://bit.ly/paineldadoscovid19.

O código disponível no github são dos scripts necessários para obter os dados e cadastrá-los no banco de dados, as visualizações da plataforma são desenvolvidas utilizando Microsoft Power BI.

![Painel 3](https://user-images.githubusercontent.com/26206052/86056446-d94caa00-ba33-11ea-9738-f8f5713fd5dd.png)

## Objetivos
O objetivo principal do projeto Painel Paraná Covid-19 é monitorar de forma inteligente os dados do coronavírus prioritariamente no estado do Paraná e no restante do Brasil, com dados atualizados em tempo real e com uso de algoritmos de inteligência artificial para executar predições e construir relatórios para tomadas de decisão por parte dos órgãos públicos e privados que atuam no combate do covid19.

Dentre alguns dos objetivos gerais do projeto estão.
  - Coletar dados sobre o covid-19 no âmbito estadual, nacional e mundial em tempo real formando uma base de dados conscistente e confiável
  - Construir esquemas de visualização da informação de modo que a interpretação dos dados seja simples e direta por parte do público
  - Monitorar a situação do coronavírus utilizando de algoritmos de inteligência artificial para executar predições acerca da quantidade de pessoas e recursos médicos que serão afetados nos dias subsquentes formando conhecimento relevante
  - Gerar relatórios técnicos com tomadas de decisão para auxiliar as os órgãos públicos e privados no combate ao covid-19

## Tecnologias

Painel Paraná Inteligente Covid-19 usa os seguintes algoritmos e tecnologias:

* [Regressão Logística](https://medium.com/turing-talks/turing-talks-14-modelo-de-predi%C3%A7%C3%A3o-regress%C3%A3o-log%C3%ADstica-7b70a9098e43) - executar predições
* [Regressão Linear](https://medium.com/@lucasoliveiras/regress%C3%A3o-linear-do-zero-com-python-ef74a81c4b84) - executar predições
* [Mínimos Quadrados](https://www.scielo.br/scielo.php?pid=S0100-40422007000200020&script=sci_arttext) - comparar predições geradas e efetuar ajustes
* [Árvores de Decisão](https://www.vooo.pro/insights/um-tutorial-completo-sobre-a-modelagem-baseada-em-tree-arvore-do-zero-em-r-python/) - gerar tomadas de decisão com base em condições pré-estabelecidas
* [Numpy](https://numpy.org/) - plotagens de dados e gráficos
* [Pandas](https://pandas.pydata.org/) - execução de algoritmos de predição
* [beautiful soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - extração automática de dados


  
