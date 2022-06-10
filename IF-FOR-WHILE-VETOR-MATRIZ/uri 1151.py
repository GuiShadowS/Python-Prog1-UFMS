# -*- coding: utf-8 -*-

"""
    Fibonacci Fácil - 1151
    n == 1: 0
    n == 2: 0 1
    n == 3: 0 1 1
    n == 4: 0 1 1 2
    n == 5: 0 1 1 2 3
"""

# n = Ler um número inteiro
n = int(input())

# se n == 1
if n == 1:
    # então Mostrar "0"
    print(0)
# senão se n == 2
elif n == 2:
    # então Mostrar "0 1"
    print("0 1")
# senão
else:
    # Mostrar "0 1" sem pular linha
    print("0 1", end = "")
    # ant1 = 0
    ant1 = 0
    # ant2 = 1
    ant2 = 1
    # para i de 3 até n
    for i in range(3, n+1):
        # prox = ant1 + ant2
        prox = ant1 + ant2
        # Mostrar " " seguido de prox, sem pular linha
        print("", prox, end = "")
        # 0     1     1
        # ant1  ant2  prox
        # ant1 = ant2
        ant1 = ant2
        # ant2 = prox
        ant2 = prox
        # 0     1     1
        #       ant1  ant2
    print()
