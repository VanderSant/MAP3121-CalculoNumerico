#!/usr/bin/env python3
#coding=utf-8

from assignments.assignment_1 import assignment_1

EP_HEADER = '''
===============================================================================================
                            MAP3121 - Métodos Numéricos e Aplicações
-----------------------------------------------------------------------------------------------
2° Exercício Programa - O Algoritmo QR

11261110 - Antonio Lago Araújo Seixas                                                 turma: 1
11259715 - Vanderson da Silva dos Santos                                              turma: 2
===============================================================================================
'''

INFO = '''
TAREFAS:
(1) Tarefa 4.1: Calculo dos autovalores e autovetores das matrizes
(2) Tarefa 4.2: Treliças Planas
'''

def print_assignment_header(letter):
    print('''\n
 ================================================================================================\n''',
'=================================== assignment {type} ==============================================='.format(type = letter),'''
 ================================================================================================\n''')

def main():
    print(EP_HEADER)
    while True:
        print(INFO,"\n")
        assignment = input("Você quer ver qual tarefa?: ")
        if ((assignment=="1") or (assignment=="4.1")):
            print_assignment_header("1")
            assignment_1()

        elif ((assignment=="2") or (assignment=="4.2")):
            print_assignment_header("2")
            #function two here

        else:
            print("your input isn't valid \nplease, try again\n")

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nBetter luck next time")
