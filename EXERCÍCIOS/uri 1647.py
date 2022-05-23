# -*- coding: utf-8 -*-

'''
Existem n bacias, numeradas de 1 até n. Inicialmente, a bacia i contém mi bolas de gude.
Uma rodada consiste em remover uma bola de gude de uma bacia.
Quando uma bola de gude é removida da bacia i (i > 1), outra bola de gude é adicionada
a cada uma das primeiras i-1 bacias; se uma bola de gude é removida da bacia 1, nenhuma
nova bola de gude é adicionada. O jogo termina quando cada uma das bacias estiver vazia.

Seu trabalho é determinar quantas rodadas são necessárias para o jogo terminar.
Você pode assumir que o suprimento de bolas de gude é suficiente,
e que todas as bacias são grandes o suficiente, de tal forma que cada rodada possível pode ser executada.
'''

# Enquanto Verdadeiro
while True:
    # n = Ler inteiro indicando o número de bacias
    n = int(input())
    
    # se n == 0
    if n == 0:
        # Sair do laço enquanto
        break
    
    # bacias = Ler a quantidade de bolas de gude em cada bacia
    sbacias = input().split()
    bacias = n*[0]
    
    for i in range(n):
        bacias[i] = int(sbacias[i])
    
    # i_bacia = 0
    i_bacia = 0
    
    # rodadas = 0
    rodadas = 0
    
    # Enquanto Verdadeiro
    while True:
        # se i_bacia == 0
        if i_bacia == 0:
            # rodadas = rodadas + bacias[0]
            rodadas = rodadas + bacias[0] 
            # bacias[0] = 0
            bacias[0] = 0
        # senão # i_bacia de 1 até n-1
        else:
            # rodadas = rodadas + bacias[i_bacia]
            rodadas = rodadas + bacias[i_bacia]
            # para j de 0 até i_bacia - 1
            for j in range(i_bacia):
                # bacias[j] = bacias[j] + bacias[i_bacia]
                bacias[j] = bacias[j] + bacias[i_bacia]
            # bacias[i_bacia] = 0
            bacias[i_bacia] = 0
        # i_bacia = (i_bacia + 1) % n
        i_bacia = (i_bacia + 1) % n
        
        # qt = 0
        qt = 0
        
        # enquanto qt < n E bacias[qt] == 0
        while qt < n and bacias[qt] == 0:
            # qt = qt + 1
            qt = qt + 1
            
        # se qt == n
        if qt == n:
            # Sair do laço enquanto
            break
    # Mostrar rodadas
    print(rodadas)
