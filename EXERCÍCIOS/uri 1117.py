# -*- coding: utf-8 -*-

'''Faça um programa que leia as notas referentes às duas avaliações
de um aluno. Calcule e imprima a média semestral.
Faça com que o algoritmo só aceite notas válidas
(uma nota válida deve pertencer ao intervalo [0,10]).
Cada nota deve ser validada separadamente.'''

# Lê a nota 1 e converte para ponto flutuante
n1 = float(input())

# Lógica para verificar se a nota está no
# intervalo de [0,10] e caso não esteja seja
# printado a mensagem de nota invalida e
# solicitado uma nova entrada de nota
while n1 < 0 or n1 > 10:
    print("nota invalida")    
    n1 = float(input())

# Lê a nota 2 e converte para ponto flutuante
# faz a mesma lógica descrita acima
n2 = float(input())

while n2 < 0 or n2 > 10:
    print("nota invalida") 
    n2 = float(input())
    
# Lógica para encontrar a média aritmética dos valores
media = (n1 + n2) / 2

# Mostra na tela o valor da média com duas casas decimais
print("media = %.2f" %media)