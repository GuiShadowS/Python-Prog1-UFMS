# -*- coding: utf-8 -*-

'''
Nesse programa iremos fazer comparações entre 3 valores fornecidos num jogo infantil
e dizer quem saiu vencedor nas comparações, muito parecido com o "pedra, papel e tesoura"
com base nas normas abaixo, será feita as verificações no código

Uma partida, com dois jogadores, possuem as seguintes regras para se definir um vencedor:

Ataque Aéreo vs. Pedra: Neste caso, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias.
Pedra vs. Papel: Neste caso, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.
Papel vs. Ataque Aéreo: Aqui o Ataque Aéreo ganha, porque Ataque Aéreo sempre ganha e o Papel é patético.
Papel vs. Papel: Nesta variação, ambos os jogadores ganham, porque o Papel é inútil e ninguém que enfrenta o Papel pode perder.
Pedra vs. Pedra: Para este caso não há ganhador, porque depende do que os jogadores decidem fazer com a Pedra e normalmente não fazem nada.
Ataque Aéreo vs. Ataque Aéreo: Quando isto acontece, todos os jogadores perdem, devido a Aniquilação Mútua.
'''

# A primeira entrada é um valor inteiro que mostrará quantas vezes o programa irá rodar
# pedindo os valores para comparação ao usuário
N = int(input())

# Agora vamos atribuir variáveis de comparação que serão usadas a seguir
pedra = 'pedra'
ataque = 'ataque'
papel = 'papel'

# Esse laço serve para rodar o programa na mesma quantidade de vezes que foi fornecido
# pelo usuário na entrada do valor inteiro N
while ((N + 1) - 1) > 0:
    # Aqui vamos receber as duas entradas informando qual foi o ataque usados pelo usuário
    atq1 = input()
    atq2 = input()

    # Essa estrutura condicional de IFs serve para fazer as comparações dos ataques
    # e descobrir quem saiu vencedor, perdedor, sem ganhador ou aniquilação mutua
    if atq1 == pedra and atq2 == pedra:
        print("Sem ganhador")
    if atq1 == papel and atq2 == papel:
        print("Ambos venceram")
    if atq1 == ataque and atq2 == ataque:
        print("Aniquilacao mutua")
        
    if atq1 == pedra and atq2 == papel:
        print("Jogador 1 venceu") 
    elif atq1 == papel and atq2 == pedra:
        print("Jogador 2 venceu")
        
    if atq1 == pedra and atq2 == ataque:
        print("Jogador 2 venceu")
    elif atq1 == ataque and atq2 == pedra:
       print("Jogador 1 venceu")
       
    if atq1 == papel and atq2 == ataque:
        print("Jogador 2 venceu")
    elif atq1 == ataque and atq2 == papel:
        print("Jogador 1 venceu")    
    
    # Essa linha serve para o controle da condição do laço While            
    N = N - 1