# -*- coding: utf-8 -*-

'''
Programa que vai identificar se a resposta de um participante de um teste as escuras sobre chás
é correta ou não, com isso o programa recebe um numero que é referente a um tipo de chá

(1) o chá branco
(2) chá verde
(3) chá preto
(4) chá de ervas    

Após isso recebe 5 valores que são as respostas de 5 participantes sobre qual é o tipo de chá
e verifica quantos participantes acertaram
'''

# Recebe o numero inteiro referente ao chá
cha = int(input())

# Recebe as respostas dos participantes
R1s, R2s, R3s, R4s, R5s = input().split()

# Declara a variável contador que irá armazenar a quantidade de acertos
contador = 0

# Converte os valores das respostas do formato 'str' para 'int'
R1 = int(R1s)
R2 = int(R2s)
R3 = int(R3s)
R4 = int(R4s)
R5 = int(R5s)

# Lógica para fazer as comparações 
if cha == 1:
    if R1 == 1:
        contador = contador + 1
    if R2 == 1:
        contador = contador + 1
    if R3 == 1:
        contador = contador + 1
    if R4 == 1:
        contador = contador + 1
    if R5 == 1:
        contador = contador + 1

elif cha == 2:
    if R1 == 2:
        contador = contador + 1
    if R2 == 2:
        contador = contador + 1
    if R3 == 2:
        contador = contador + 1
    if R4 == 2:
        contador = contador + 1
    if R5 == 2:
        contador = contador + 1

elif cha == 3:
    if R1 == 3:
        contador = contador + 1
    if R2 == 3:
        contador = contador + 1
    if R3 == 3:
        contador = contador + 1
    if R4 == 3:
        contador = contador + 1
    if R5 == 3:
        contador = contador + 1

else:
    cha == 4
    if R1 == 4:
        contador = contador + 1
    if R2 == 4:
        contador = contador + 1
    if R3 == 4:
        contador = contador + 1
    if R4 == 4:
        contador = contador + 1
    if R5 == 4:
        contador = contador + 1
    
print(contador)