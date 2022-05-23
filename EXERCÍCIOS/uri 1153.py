# -*- coding: utf-8 -*-

'''Ler um valor N. Calcular e escrever seu
respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1. '''

# Lê um numero inteiro N (0<N<13)
n = int(input())

# Declara uma variável para receber o valor
# do fatorial
fatorial = 1

# Lógica para calcular o fatorial do valor N
while n >= 1:
    fatorial = fatorial * n
    n = n - 1

# imprime na tela o resultado
print(fatorial)