# -*- coding: utf-8 -*-

'''
A entrada é composta por vários casos de teste. A primeira linha contém um número inteiro T (2 <= T <= 99) 
relativo ao número de casos de teste. As T linhas seguintes possuem três valores inteiros 
A (A < 0), B e C (-100 <= B, C <= 100), representando os coeficientes de uma 
função de segundo grau, na forma ax2 + bx + c.
'''

# Aqui lemos a quantidade de casos de teste que sera usada no programa
T = int(input())

# Esse laço serve para rodar o programa na mesma quantidade de vezes que foi fornecido
# pelo usuário na entrada do valor inteiro T
while ((T + 1) - 1) > 0:
    
    # Aqui vamos receber as entradas pelo usuário em formato 'str'
    As, Bs, Cs = input().split()

    # Vamos converter as entradas para 'int'
    A = int(As)
    B = int(Bs)
    C = int(Cs)

    # Declaramos as variáveis que serão usadas
    delta = 0
    X = 0

    # Aqui é feito o calculo do valor de delta com base nos valores fornecidos
    # e na lógica de Bhaskara
    delta = ((B * B) - 4 * A * C)
    
    # Agora com o valor de delta, vamos achar o valor de X, dividindo o delta pela multiplicação de A por 4
    X = - (delta / (A * 4))

    # Mostra na tela a saida com duas casas decimais
    print("%.2f" %X)
    
    # Essa linha serve para o controle da condição do laço While            
    T = T - 1