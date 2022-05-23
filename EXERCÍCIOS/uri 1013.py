# -*- coding: utf-8 -*-

'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
maior AB = (a+b+abs(a-b)) / 2
Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.
'''
# Utilização da biblioteca math
import math

# Le o valor de entrada e guarda na variavel valor
valor = input().split(" ")

# Atribui o valor de entrada para as variaveis a, b, c
a, b, c = valor

# Lógica para chegar no resultado com base na formula descrita no começo
maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

# Mostra na tela o resultado
print("%d eh o maior" %resultado)