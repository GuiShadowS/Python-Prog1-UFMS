# -*- coding: utf-8 -*-

'''
Recebe um numero inteiro e converte ele para saber 
quantos segundos, minutos e horas o mesmo corresponde
'''

# Recebe um numero inteiro do usuário
N = int(input())

# Atribui o valor recebido para a variável segundos
segundos = N

# Para saber quantas horas, pega-se o 
# valor de N e divide por 3600
horas = segundos // 3600

# Agora salva o resto da divisão 
# de segundos por 3600
segundos = segundos % 3600

# Para saber quantos minutos, pega o 
# valor de N e divide por 60
minutos = segundos // 60

# Para saber os segundos pega o próprio 
# valor atribuido acima e salva 
# o resto da divisão dele por 60
segundos = segundos % 60

# Mostra na tela os valores de horas
# minutos e segundos separados por dois pontos :
print(horas,minutos,segundos, sep=":")

