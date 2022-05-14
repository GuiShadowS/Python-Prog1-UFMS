# -*- coding: utf-8 -*-

'''
O Programa vai receber varios casos de teste que são entradas
de 20 numeros inteiros, e só vai finalizar quando encontrar um
err EOF, sendo que o programa vai ler qual é o
menor numero lido nos 10 primeiros e depois qual o maior numero
nos outros 10 interiros, e após isso efetua a média entre os dois numeros
'''

# Começamos com uma estrutura de repetição que irá repetir até encontrar o EOFError
while True:
    try:
        # Atribuimos uma variável para utilizar no laço a seguir
        cont = 0

        # Nesse laço, será executado 10 repetições com os valores fornecidos pelo usuario
        # e verificado qual o menor valor digitado, salvando ele na variavel menor
        while cont < 10:
            x = int(input())

            if cont == 0:
                menor = x
            else:
                if menor > x:
                    menor = x
            cont = cont + 1
        
        # Atribuimos novamente uma variável para utilizar no laço a seguir
        cont = 0

        # Nesse laço, será executado 10 repetições com os valores fornecidos pelo usuario
        # e verificado qual o maior valor digitado, salvando ele na variavel maior
        while cont < 10:
            x = int(input())

            if cont == 0:
                maior = x
            else:
                if maior < x:
                    maior = x
            cont = cont + 1
        
        # Agora será feito o calculo da média artmética dos valores encontrados
        media = (maior + menor) / 2

        # Aqui será mostrado a saida da média com apenas uma casa decimal
        print("%.1f"%media)

    # Aqui é a linha de comando para encontrar e tratar o fim de arquivo EOFError
    except EOFError:
        # Após encontra-lo utilizo o break para finalizar o programa
        break