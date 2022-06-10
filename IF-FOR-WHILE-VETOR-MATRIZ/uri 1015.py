# -*- coding: utf-8 -*-

'''Leia os quatro valores correspondentes aos eixos x e y
de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2)
e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula'''

# Lê os valores de entrada separados por espaço
x1s, y1s = input().split()
x2s, y2s = input().split()

# Converte os valores str em ponto flutuante
x1 = float(x1s)
y1 = float(y1s)
x2 = float(x2s)
y2 = float(y2s)

# Agora fazemos os calculos conforme fórmula fornecida na questão
# e salvamos o resultado na variável "calc"
calc = (((x2 - x1)**2) + ((y2 - y1)**2)) ** 0.5


# Resultado sendo impresso na tela com quatro casas decimais
print ("%0.4f" %calc)