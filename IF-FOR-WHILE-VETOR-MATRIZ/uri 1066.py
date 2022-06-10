# -*- coding: utf-8 -*-

'''Leia 5 valores Inteiros. A seguir mostre quantos valores digitados
foram pares, quantos valores digitados foram ímpares
quantos valores digitados foram positivos
e quantos valores digitados foram negativos'''

# Entrada de 5 valores inteiros, salvos nas variáveis a seguir
v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())

# Lógica para verificar se é par
par = 0

if v1 % 2 == 0:
    par = par + 1

if v2 % 2 == 0:
    par = par + 1
    
if v3 % 2 == 0:
    par = par + 1

if v4 % 2 == 0:
    par = par + 1

if v5 % 2 == 0:
    par = par + 1
    
# Lógica para verificar se é ímpar
impar = 0

if v1 % 2 != 0:
    impar = impar + 1

if v2 % 2 != 0:
    impar = impar + 1
    
if v3 % 2 != 0:
    impar = impar + 1

if v4 % 2 != 0:
    impar = impar + 1

if v5 % 2 != 0:
    impar = impar + 1
    
# Lógica para verificar se é positivo
positivo = 0

if v1 > 0:
    positivo = positivo + 1

if v2 > 0:
    positivo = positivo + 1
    
if v3 > 0:
    positivo = positivo + 1

if v4 > 0:
    positivo = positivo + 1

if v5 > 0:
    positivo = positivo + 1
    
# Lógica para verificar se é negativo
negativo = 0

if v1 < 0:
    negativo = negativo + 1

if v2 < 0:
    negativo = negativo + 1
    
if v3 < 0:
    negativo = negativo + 1

if v4 < 0:
    negativo = negativo + 1

if v5 < 0:
    negativo = negativo + 1
    
# Mostra na tela a quantidade de valores pares
print (par, "valor(es) par(es)")

# Mostra na tela a quantidade de valores ímpares
print (impar, "valor(es) impar(es)")

# Mostra na tela a quantidade de valores positivos
print (positivo, "valor(es) positivo(s)")

# Mostra na tela a quantidade de valores positivos
print (negativo, "valor(es) negativo(s)")