# -*- coding: utf-8 -*-

'''
Programa vai receber um valor N maior que 0 e menor que 100, referente a uma nota
 de aluno, e depois disso mostrará sua equivalencia na tabela de notas americanas
 com base na tabela abaixo:

 0          E
 1 a 35     D
 36 a 60    C
 61 a 85    D
 86 a 100   A
'''

from socket import INADDR_ALLHOSTS_GROUP

# Entrada do valor de N referente a nora do aluno
N = int(input())

# Nesse bloco de if, sera feito a veificação de qual posição se encaixa 
# a nota do aluno e após isso mostrado na tela a letra correspondente
if N == 0:
    print("E")
elif N >= 1 and N <= 35:
    print("D")
elif N >= 36 and N <= 60:
    print("C")
elif N >= 61 and N <= 85:
    print("B")
else:
    print("A")
