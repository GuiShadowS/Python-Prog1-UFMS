# -*- coding: utf-8 -*-

'''
Entrada
A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T indicando o número de instâncias.

A primeira (e única) linha de cada instância contém um inteiro N seguido de K pontos de exclamação, onde 1 ≤ N ≤ 100 e 1 ≤ K ≤ 20.

Saída
Para cada instância imprima uma linha contendo o K-fatorial de N.

É garantido que nenhuma instância na entrada possui resultado maior que 1018.
'''

t = int(input())

while t > 0:
    t -= 1
    f = input()
    n = ''
    k = 0
   
    while True:
        if(f[k] != '!'):
            n += f[k]
            k += 1
        else:
            n = int(n)
            k = len(f) - k
            break
   
    f = 1
    for i in range(n, 1, -k):
        f *= i
    print(f)
