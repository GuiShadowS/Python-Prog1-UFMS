# -*- coding: utf-8 -*-

"""
    Problema 1198 do URI - O Bravo Guerreiro Hashmat
    Entrada:
    A entrada contém dois números inteiros em cada
    linha. Estes dois números denotam respectivamente
    a quantidade de soldados do exército de Hashmat
    e do seu oponente.  Nenhum número de entrada é
    maior do que 2³². A entrada termina com fim
    de arquivo (EOF).
    Saída:
    Para cada linha de entrada imprima a diferença
    entre o número de soldados de Hashmat e do seu
    oponente. Cada saída deve ser impressa em uma
    linha separada.    
"""

while True: # Continua a repetir o bloco de instruções
            # a seguir até que o break seja executado
    try:    # Inicia o bloco que irá englobar
            # a sentença que pode gerar a exceção EOFError
        valores = input()
    except EOFError: # O EOF foi encontrado por input()
        break # Sai do while e termina o programa  

    sH, so = valores.split()
    nsH = int(sH)
    nso = int(so)
    # O abs() retorna o valor absoluto do número passado
    # como parâmetro e é necessário porque supera a
    # pegadinha que existe entre a ordem de entrada
    # da quantidade de soldados na entrada e a ordem
    # que os dois valores são subtraídos na saída
    # do problema.
    print(abs(nso - nsH))