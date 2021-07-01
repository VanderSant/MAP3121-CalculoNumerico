#!/usr/bin/env python3
#coding=utf-8

from assignments.assignment_a import assignment_a
from assignments.assignment_b import assignment_b
from assignments.assignment_c import assignment_c

EP_HEADER = '''
===============================================================================================
                            MAP3121 - Métodos Numéricos e Aplicações
-----------------------------------------------------------------------------------------------
1° Exercício Programa - O Algoritmo QR

11261110 - Antonio Lago Araújo Seixas                                                 turma: 1
11259715 - Vanderson da Silva dos Santos                                              turma: 2
===============================================================================================
'''
INFO = '''
TAREFAS:
(a) Tarefa A: Matriz com diagonal e subdiagonal constantes
(b) Tarefa B: Sistema Massa Mola com 5 massas
(c) Tarefa C: Sistema Massa Mola com 10 massas
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
        if ((assignment=="a") or (assignment=="A")):
            print_assignment_header("A")
            assignment_a()

        elif ((assignment=="b") or (assignment=="B")):
            print_assignment_header("B")
            assignment_b()

        elif ((assignment=="c") or (assignment=="C")):
            print_assignment_header("C")
            assignment_c()

        else:
            print("your input isn't valid \nplease, try again\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBetter luck next time")
