# -*- coding: utf-8 -*-

'''
Programa vai receber intervalos de numeros inteiros fornecidos pelo
usuário e verificar cada inteiro para saber se ele é par, ímpar
ou divisível por 5 e mostrar também quantos numeros inteiros tem 
nesse intervalo
Caso a quantidade de numeros divisiveis por 5 for par o programa para a execução
e não recebe mais intervalos de numeros do usuário
'''
# Variável que vai servir de condição para o while a seguir
div = 1

# Aqui uso uma estrutura de repetição while que vai rodar
# até que a minha condição seja falsa
while div % 2 != 0:
    # Aqui eu recebo do usuário o intervalo de inteiros
    xs, ys = input().split()

    # Faço a conversão dos valores que estão em str para int
    x = int(xs)
    y = int(ys) 
    
    # Declaração de variáveis que serão usadas na lógica a seguir do meu for
    inteiros = 0
    par = 0
    impar = 0
    div = 0   
    i = x
    
    # Aqui faço um for para analisar o intervalo de inteiros 
    # e verificar quantos numeros inteiros tem excluindo os fornecidos pelo usuário
    # verifico a quantidade de pares, impares e divisiveis por 5
    # usando a lógica da divisão usando o módulo    
    for x in range (x + 1, y):
        inteiros = inteiros + 1
        if x % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
        if x % 5 == 0:
            div = div + 1
    
    # Aqui as saídas conforme solicitado no exercicio
    # pulando linha após cada caso de teste            
    print("Intervalo (%d, %d):"%(i,y))
    print("Quantidade de inteiros:",inteiros)
    print("Quantidade de pares:",par)
    print("Quantidade de ímpares:",impar)
    print("Quantidade de divisíveis por 5:",div)
    if div % 2 != 0:
        print("")