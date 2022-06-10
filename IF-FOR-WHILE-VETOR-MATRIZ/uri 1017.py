# -*- coding: utf-8 -*-

'''Programa para calcular a quantidade de litros de combustivel
gastos em uma viagem, utilizando um automóvel que faz 12 km/L'''

# Recebe a quantidade de horas gastas na viagem
horas = int(input())

# Recebe o valor da velocidade média gasta
vel = int(input())

# Faz o calculo da quantidade de litros necessarios
# pega a quantidade de horas multiplica pela velocidade
# depois divide pelo valor que o carro faz por cada KM/L no caso 12
litros = (horas * vel) / 12

# Mostra na tela o resultado com três casas decimais
print ("%0.3f" %litros)