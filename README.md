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
## Instação das bibliotecas

Biblioteca [OR-Tools](https://developers.google.com/optimization/install)<br>
`python -m pip install --upgrade --user ortools`

Pacote [igraph](https://igraph.org/python/)<br>
`pip install python-igraph`


### Pode ser necesário a instalção do módulo [Pycairo](https://pypi.org/project/pycairo/)
`pip install pycairo`

## Execução do Código

* De preferência esteja usando sistema operacional Ubuntu 18.04, ou Windows 10
* Entre no diretório que esta o código
* Abra um terminal e digite o comando:
  ``python codigo.py`
  
  ## Visualização da resposta
  Será aberta uma janela com a imagem e seram impressos no terminal os dados da resposta.<br><br>
  
  Obs. Foi usado o linear optimization solve da OR-Tools, o [Glop](https://developers.google.com/optimization/lp/glop) (Google's linear programming system). Sendo ele eficiente em questão de velocidade para resolver o problema e alocação de memória, além de ser numericamente estável. 

