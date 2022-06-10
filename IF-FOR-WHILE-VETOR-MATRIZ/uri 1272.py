# -*- coding: utf-8 -*-

'''
Programa que vai receber um numero inteiro que vai determinar quantas vezes será rodado o programa
e após isso irá receber uma sequencia de caracteres como os do exemplo a seguir:

compete·online·design·event·rating          --> coder
··u····r·i··o····n·l··i····n··e···          --> urionline
·                                           --> não mostra nada
round··elimination·during··onsite··contest  --> redoc

em que cada ponto (.) se refere a um espaço, aparecendo apenas para facilitar a visão da questão
e após isso mostrar cada primeira letra que compoem cada string lida e mostrar na tela o resultado
'''

# Aqui vamos ler um numero inteiro que será o responsável por dizer quantas vezes o programa irá rodar
N = int(input())

# Esse laço usa o numero inteiro lido anteriormente como condição para rodar o programa até a quantidade
# de vezes especificada
while N > 0:
    # Nessa linha vamos receber a string e já salva-la como uma lista
    lista = input().split()

    # Aqui declaramos a variável que será usada para montar a palavra final
    msg = ""

    # Variável tamanho recebe o tamanho da lista que foi criada
    tamanho = len(lista)
    
    # Esse if usa o tamanho da lista como condição para rodar
    for i in range (tamanho):
        # Aqui declaramos uma palavra que irá receber as strings que compoem a lista, começando na posição 0
        palavra = lista[i]
        # Nessa parte vamos salvar na variável msg o primeiro caractere da primeira string salva na lista
        # e ir concatenando os outros primeiros caracteres das outras strings lidas, até formar a palavra desejada
        msg = msg + palavra[0]

    # Mostramos na tela a palavra formada    
    print(msg)

    # Essa lógica é para controlar o laço e faze-lo parar assim que N for igual a 0
    N = N - 1