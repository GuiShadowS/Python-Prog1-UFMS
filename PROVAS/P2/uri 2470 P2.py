# -*- coding: utf-8 -*-

'''
Faça um programa que leia um valor N referente as posições do vetor
após isso leia os valores do vetor 'N' vezes, e leia mais dois valores
que serão a posição no vetor e a quantidade de posições que serão
afetadas pela bomba
'''

# N = Ler o tamanho do vetor
N = int(input())

# lista_orig = Ler o vetor de inteiros
linha = input().split() # Ler a lista de strings
lista_orig = [0]*N # Gerar a lista de inteiros

# Transforma cada cada string de linha em um valor
# int e o armazena na posição correspondente em
# lista_orig
for i in range(N):
    lista_orig[i] = int(linha[i])
    
# lista = Cópia de lista_orig
lista = lista_orig.copy()

# Ler I e A
IA = input().split()
I = int(IA[0])
A = int(IA[1])

# inicio = I - A
inicio = I - A

# Se o inicio extrapola o menor índice válido
if inicio < 0:
    # Faça inicio = 0
    inicio = 0

# fim = I+A
fim = I+A

# Se o fim extrapola o maior índice válido
if fim > N-1:
    # Faça fim = N-1
    fim = N-1

# i = inicio
i = inicio

# O laço while irá percorrer cada posição
# de lista de inicio a fim
while i <= fim:
    # lista[i] = 0
    lista[i] = 0
    # i += 1
    i += 1

# Mostra os valores da lista_orig até o
# penúltimo valor, com largura 3 e espaçamento,
# sem pular linha.
for i in range(N-1):
    print("{0:3d} ".format(lista_orig[i]), end="")
# Mostra o último valor de lista_orig, com largura 3
print("{0:3d}".format(lista_orig[N-1]))

# Mostra os valores da lista até o
# penúltimo valor, com largura 3 e espaçamento,
# sem pular linha.
for i in range(N-1):
    print("{0:3d} ".format(lista[i]), end="")
# Mostra o último valor de lista, com largura 3
print("{0:3d}".format(lista[N-1]))
