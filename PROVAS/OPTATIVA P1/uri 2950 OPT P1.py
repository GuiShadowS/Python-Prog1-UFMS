# -*- coding: utf-8 -*-

'''
Após receber os 3 valores de entrada seguindo a orientação de que o N seja maior que 0
e menor que 10000, o X ser maior que zero e o Y ser menor que 100
o programa vai calcular o ICM (Interferencia de comunicação magica) com a seguinte fórmula
ICM = N / (X + Y) pegando a divisão com casa decimal
'''

# Aqui recebemos do usuário as informações referentes a distancia e os diâmetros dos Palantír's
# porém toda a informação esta em formato 'str'
Ns, Xs, Ys = input().split()

# Agora com os dados obtidos eu faço a conversao dos 'str' para 'int'
N = int(Ns)
X = int(Xs)
Y = int(Ys)

# A lógica para saber o ICM é a seguinte: dividir a distancia pela soma dos diametros
# e armazenar o valor com ponto decimal em ICM
ICM = N / (X + Y)

# Agora mostramos na tela o resultado com duas casas decimais
print("%.2f"%ICM)