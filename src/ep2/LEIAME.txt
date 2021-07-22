# EP2 - Autovalores e Autovetores de Matrizes Reais Simétricas - O Algoritmo QR

Engenharia Elétrica - Escola Politécnica da Universidade de São Paulo
11261110 - Antonio Lago Araújo Seixas                                                 turma: 1
11259715 - Vanderson da Silva dos Santos                                              turma: 2

## Execução:
Para executar o Exercício Programa 2, vá para o diretório  onde se encontra o arquivo "main.py" e o execute-o com o comando "python main.py".

Ao executar o arquivo, será questionado qual tarefa deseja-se executar, com isso, digite:

  1 - Caso deseje visualizar a execução da tarefa 1 - Testes

  2 - Caso deseje visualizar a execução da tarefa 2 - Aplicação: Treliças Planas

Na tarefa 1, temos opção de observar o item 1.a ou 1.b, com isso, digite:

  a - Tarefa 4.1.a: Calculo dos auto valores e autovetores da matriz:
                    [2., 4., 1., 1.]
                    [4., 2., 1., 1.]
                    [1., 1., 1., 2.]
                    [1., 1., 2., 1.]

  b - Tarefa 4.1.b: Calculo dos auto valores e autovetores da matriz:
                    [ n  n-1 n-2 ...  2   1 ]
                    [n-1 n-1 n-2 ...  2   1 ]
                    [n-2 n-2 n-2 ...  2   1 ]
                    [ :   :   :  ...  :   : ]
                    [ 2   2   2   2   2   1 ]
                    [ 1   1   1   1   1   1 ]

## Estrutura dos arquivos

  __QR_algorithm.py__             - Declaração das funções referente a execução ao algoritmo QR
  __householder_algorithm.py__    - Declaração das funções referentes a execução das transformações de Householder
  __assignment_1.py__             - Declaração das funções necessárias a execução da tarefa 1
  __assignment_2.py__             - Declaração das funções necessárias a execução da tarefa 2
  __main.py__                     - Função principal a qual executa o EP
  __plot_functions.py__           - Biblioteca utilizada para construção de gráficos

  input-a/b/c                    - Dados fornecidos pela disciplina necessários a execução do EP
