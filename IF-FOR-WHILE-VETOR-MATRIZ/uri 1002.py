# -*- coding: utf-8 -*-

'''
Após receber um valor com casa decimal fornecido 
pelo usuário, deve-se fazer o calculo da area 
de um circulo, usando a fórmula, area = n * raio ao quadrado
com o valor de n = 3.14159
'''

# Leia o valor com ponto flutuante
raio = float(input())
n = 3.14159

# Com o valor do raio recebido, deve-se efetuar 
# o calculo, substituindo os valores na fórmula 
# apresentada no começo do exercicio
area = n * (raio * raio)

# Mostra na tela o resultado da operação 
# com o fim de linha solicitado
print("A=%.4f"%(area))