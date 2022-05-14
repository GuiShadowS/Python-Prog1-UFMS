# -*- coding: utf-8 -*-

'''
Recebe dois valores com casa decimal que são as 
notas de um aluno, depois calcule a média ponderada
das notas usando o peso 3.5 para a primeira nota
e o peso 7.5 para a segunda nota, sabendo que 
cada nota deve estar no intervalo de 0 a 10
'''

# Leia dos dois valores com casa decimal referente as notas
n1 = float(input())
n2 = float(input())

# Agora vamos multiplicar o valor de cada 
# nota pelo seu respectivo peso
# depois somar os valores e dividir pela soma dos pesos
media = ((n1 * 3.5) + (n2 * 7.5)) / 11

# Imprime na tela a media com 5 casas decimais
print("MEDIA = {0:.5f}".format(media))