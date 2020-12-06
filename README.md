# Trabalho da Disciplina SME0110 

<p align="center">
  Disciplina SME0110 - Programação Matemática
</p>

Alunos: <br>
[Angelo A. R. Tessaro](https://github.com/angelotessaro) <br>
[Bruno Mitsuo Homma](https://github.com/brunohomma) <br>
[Leandro Antonio Silva](https://github.com/leandroS08) <br>
[Marilene Andrade Garcia](https://github.com/MarileneGarcia)


<!-- TABLE OF CONTENTS -->
## Informações sobre o trabalho

* [Descrição do trabalho](Trabalho.pdf)
* [Relatório da primeira etapa](Relatorio.pdf)
* [Instação das bibliotecas](#instação-das-bibliotecas)<br>
* [Execução do código](#execução-do-código)
* [Visualização da resposta](#visualização-da-resposta)


<!-- ABOUT THE PROJECT -->
## Instalação das bibliotecas

Biblioteca [OR-Tools](https://developers.google.com/optimization/install)<br>
`python -m pip install --upgrade --user ortools`

Pacote [igraph](https://igraph.org/python/)<br>
`pip install python-igraph`

Biblioteca [numpy](https://numpy.org/doc/stable/)<br>
`pip install numpy`

Biblioteca [matplotlib](https://matplotlib.org/contents.html)<br>
`pip install matplotlib`

Biblioteca [itertools](https://docs.python.org/3/library/itertools.html)<br>
`pip install itertools`




##### Pode ser necesário a instalação do módulo [Pycairo](https://pypi.org/project/pycairo/)
`pip install pycairo`

## Execução do Código

* De preferência esteja usando sistema operacional Ubuntu 18.04, ou Windows 10
* Entre no diretório que esta o código

Para a primeira parte do trabalho, com 5 galáxias pré-definidas ou com número personalizado de galáxias geradas aleatoriamente:

* Abra um terminal e digite o comando:<br>
`python main.py`

É possível escolher a opção do caso exemplo (0) ou personalizar um número de galáxias (1):

`---> Digite 0 para o caso exemplo e 1 para personalizar: `

Para a heurística de Vizinhos Próximos:

* Abra um terminal e digite o comando:<br>
`python vizinhos_proximos.py`

Serão listadas as instâncias possíveis, basta selecionar a desejada:

`---> Digite 0 para Djibouti, 1 para Qatar, 2 para Uruguay e 3 para Western Sahara:`

Para a heurística 2-opt:

* Abra um terminal e digite o comando:<br>
`python 2-opt.py`

Serão listadas as instâncias possíveis, basta selecionar a desejada:

`---> Digite 0 para Djibouti, 1 para Qatar, 2 para Uruguay e 3 para Western Sahara:`

Para as ferramentas prontas do OR-Tools:

* Abra um terminal e digite o comando:<br>
`python or-tools.py`

Serão listadas as instâncias possíveis, basta selecionar a desejada:

`---> Digite 0 para Djibouti, 1 para Qatar, 2 para Uruguay e 3 para Western Sahara:`



 ## Visualização da resposta
 Será aberta uma janela com a representação gráfica e serão impressos no terminal os dados da resposta.<br><br>
  
 ### Obs. 
 Foi usado o linear optimization solve da OR-Tools, o [Glop](https://developers.google.com/optimization/lp/glop) (Google's linear programming system). Sendo ele eficiente em questão de velocidade para resolver o problema e alocação de memória, além de ser numericamente estável. 

