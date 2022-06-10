# -*- coding: utf-8 -*-

"""
    Soma de Ímpares Consecutivos I - 1071
    Ler os números inteiros x e y.
    Colocar o menor deles em uma variável inicio
    e o maior deles em uma variável fim.
    Garantir que o inicio seja ímpar, mas que não
    seja o menor valor dado.
    Fazer uma laço de inicio até fim, somando
    os valores ímpares, sem incluir o fim.
    Mostrar a soma.
"""

# x = Ler número inteiro
x = int(input())
# y = Ler número inteiro
y = int(input())

# se x == y
if x == y:
    # então Mostrar 0
    print(0)
# senão
else:
    # se x < y
    if x < y:
        # então inicio = x
        inicio = x
        # fim = y
        fim = y
    else:
    # senão se x > y
        # inicio = y
        inicio = y
        # fim = x
        fim = x
        
    # se inicio for ímpar
    if inicio % 2 != 0:
        # então inicio = inicio + 2
        inicio = inicio + 2
    # senão
    else:
        # inicio = inicio + 1
        inicio = inicio + 1
        
    # se fim for ímpar
    if fim % 2 != 0:
        # então fim = fim - 2
        fim = fim - 2
    # senão
    else:
        # fim = fim - 1
        fim = fim - 1

    # soma = 0
    soma = 0

    """
    # para i de inicio até fim, passo 2
    for i in range(inicio, fim+1, 2):
        # soma = soma + i
        soma = soma + i
    """
    i = inicio
    while i <= fim:
        soma = soma + i
        i += 2

    # Mostrar soma
    print(soma)

