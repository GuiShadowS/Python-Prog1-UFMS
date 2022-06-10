# -*- encoding: utf-8 -*-

'''Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares
consecutivos a partir de X, um valor por linha, inclusive o X
ser for o caso'''

# Leia o valor inteiro fornecido
X = int(input())

# Lógica para apresentar os valores ímpares
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0

if X % 2 != 0:
    i1 = X 
    i2 = X + 2
    i3 = X + 4
    i4 = X + 6
    i5 = X + 8
    i6 = X + 10
else:
    X % 2 == 0
    i1 = X + 1
    i2 = X + 3
    i3 = X + 5
    i4 = X + 7
    i5 = X + 9
    i6 = X + 11
    
# Imprime na tela os valores, cada um em uma linha
print (i1)
print (i2)
print (i3)
print (i4)
print (i5)
print (i6)
        