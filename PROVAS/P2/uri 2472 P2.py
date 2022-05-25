# -*- coding: utf-8 -*-

'''
Seu programa deverá ler dois vetores de números inteiros,
informar se há interseção entre os dois vetores
e mostrar os valores de interseção se existirem.
Assuma que não há valores repetidos dentro de cada vetor lido.
O vetor que servirá para mostrar os elementos de interseção
deve ter apenas a quantidade exata de posições correspondente
aos valores que aparecem simultaneamente nos dois vetores lidos.
'''

# T1 = Ler o tamanho do primeiro vetor
T1 = int(input())

# V1 = Ler o primeiro vetor de inteiros
v = input().split()
V1 = T1*[0]
for i in range(T1):
    V1[i] = int(v[i])

# T2 = Ler o tamanho do segundo vetor
T2 = int(input())

# V2 = Ler o segundo vetor de inteiros
v = input().split()
V2 = T2*[0]
for i in range(T2):
    V2[i] = int(v[i])

# n recebe o menor tamanho entre T1 e T2
# para armazenar os valores de interseção
if T1 < T2:
    n = T1
else:
    n = T2

# pre_inter = vetor de n posições para os
# valores de interseção
pre_inter = n*[0]

# ind_inter será utilizado como índice de pre_inter
# e como quantidade de elementos de interseção
# ind_inter = 0
ind_inter = 0

# Os dois laços para servem para procurar
# cada elemento do primeiro vetor no segundo vetor
# para i de 0 a T1-1
for i in range(T1):
    # para j de 0 a T2-1
    for j in range(T2):
        # se V1[i] == V2[j]
        if V1[i] == V2[j]:
            # pre_inter[ind_inter] = V1[i]
            pre_inter[ind_inter] = V1[i]
            # ind_inter += 1
            ind_inter += 1
            # Se achou, já pode sair do segundo laço para
            break

# Se a quantidade de interseções ind_inter for
# menor que n então criamos um vetor inter com 
# exatamente ind_inter posições e colocamos
# os elementos de interseção em inter

# se ind_inter < n
if ind_inter < n:
    # n = ind_inter
    n = ind_inter
    # inter = n*[0]
    inter = n*[0]
    # para i de 0 a n-1
    for i in range(n):
        # inter[i] = pre_inter[i]
        inter[i] = pre_inter[i]
# senão
else:
    # inter = pre_inter
    inter = pre_inter

# se n == 0
if n == 0:
    # Mostrar "Não há interseção!"
    print("Não há interseção!")
# senão
else:
    # Mostrar "Elementos de interseção:"
    print("Elementos de interseção:")
    # elementos = ""
    elementos = ""
    # para i de 0 a n-2
    for i in range(n-1):
        # elementos += str(inter[i]) + " "
        elementos += str(inter[i]) + " "
    # elementos += str(inter[n-1])
    elementos += str(inter[n-1])
    # Mostrar elementos
    print(elementos)