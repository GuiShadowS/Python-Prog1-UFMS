# -*- coding: utf-8 -*-

'''
Esse programa vai receber um intervalo de valores de M e N, se algum dos valores for menor
ou igual a zero o programa se encerra, caso contrario ele verifica qual é o menor
valor entre ambos e a partir dali começa a imprimir na tela a sequencia numeroca em ordem
crescente do menor valor até o maior valor, considerando ambos e após isso faz o calculo
de todos os numeros que estão nesse intervalo considerando os dois fornecidos pelo usuário 
e mostra na tela o resultado
'''

# Laço sempre vai ser verdadeiro ate que a condição dentro dele seja False
# quando isso acontecer ele para o programa
while True:
    
    # Aqui recebemos os valores do usuario que sao salvos como 'str'
    Ms, Ns = input().split()
    
    # Aqui fazemos a conversão desses 'str' em 'int'    
    M = int(Ms)
    N = int(Ns)
    
    # Essa linha é a condição que vai dizer se o programa vai continuar rodando ou vai para
    # Ele verifica se algum dos valores fornecidos é igual ou menor que 0
    # se for ele para o programa
    if M <= 0 or N <= 0:
        break
    
    # Aqui declaramos as variáveis que serão usadas nas logicas abaixo
    # para saber o menor e maior valor e para ser usada no calculo da soma
    soma = 0
    maior = 0
    menor = 0
    
    
    # Nesse bloco de If eu verifico qual é o menor valor e guardo ele na variavel menor
    # Tambem verifico o maior valor e guardo na variável maior
    if M > N:
        maior = M
        menor = N
    else:
        maior = N
        menor = M
    
    # Essa estrutura de repetição é a responsavel por fazer a verificação dos valores
    # e ir armazenando na variavel correspondente e ja ir imprimindo na tela os valores em ordem crescente
    # junto ja faz a soma de todos os valores lidos
    for i in range (menor, maior + 1):
        soma = soma + i
        
        # Esse print mostra a sequencia de numeros em ordem crescente separados por espaço
        print(i, end=" ")
        
    # Esse print entra fora da estrutura de repetição para poder mostrar na tela apenas o valor da soma
    print("Sum=%d" %soma)