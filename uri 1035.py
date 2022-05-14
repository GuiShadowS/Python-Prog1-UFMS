# -*- coding: utf-8 -*-

'''
Recebe 4 valores do usuário e faz várias verificações
para saber se os valores são aceitos ou não
'''

# Le 4 valores inteiros forncecidos pelo usuário na mesma linha
As, Bs, Cs, Ds = input().split()

# Converte os 4 valores que foram recebidos como str para int
A = int(As)
B = int(Bs)
C = int(Cs)
D = int(Ds)

# Lógica com if para fazer as comparações necessárias
if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0:
    # Mostra na tela a mensagem abaixo caso toda a linha acima seja True
    print("Valores aceitos")
else:
    # Caso tenha algum caso falso, imprime a mensagem abaixo
    print("Valores nao aceitos")