# -*- coding: utf-8 -*-

'''Leia um valor N e mostre a tabuada do mesmo de 1 a 10'''

# Digite o valor de N
N = int(input())

# Lógica para fazer a tabuada e imprimir na tela o resultado
# Nela eu falo que no intervalo de 1 a 10 eu quero fazer
# uma multiplicação do valor de N pelo i (que vai de 1 a 10)
# e imprimir na tela o resultado dessa multiplicação
for i in range(1, 11):
    print("{} x {} = {}".format(i , N , i * N))