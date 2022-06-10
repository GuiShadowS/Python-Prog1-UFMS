# -*- coding: utf-8 -*-

'''
Faça um programa que leia um vetor A[100]. 
No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 
e o valor armazenado em cada uma das posições.
'''

# Criamos um vetor vazio que receberá os valores digitados
A = []

# Aqui faremos o for percorrer todas as posições do vetor
for i in range(100):
    # adicionando o numero digitado em formato de ponto flutuante
    x = float(input())
    # Aqui pegamos o valor digitado e adicionamos ao final da lista vazia
    # Que no caso é a primeira posição
    A.append(x)
    
    # Aqui fazemos a comparação do valor digitado, caso seja menor ou igual a 10
    # Ele é mostrado na tela  junto com sua posição no vetor
    if x <= 10.0:
        print('A[{}] = {}'.format(i,x))