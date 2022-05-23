# -*- coding: utf-8 -*-

'''Leia 100 valores inteiros.
Apresente então o maior valor lido
e a posição dentre os 100 valores lidos.'''

# Lê a entrada fornecida pelo usuário
numero = int(input())
x = 0

# Lógica para verificar os numeros e ver
# qual foi o maior e em qual posição
# o mesmo está
for i in range(1,100):
    a = int(input())
    if a > x:
        maior = a
        posicao = i + 1
        x = a

# Imprime na tela as saídas conforme solicitado
# no problema
print(maior)
print(posicao)