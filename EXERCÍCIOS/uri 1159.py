# -*- coding: utf-8 -*-

'''O programa deve ler um valor inteiro X indefinidas
vezes. (O programa irá parar quando o valor de X
for igual a 0). Para cada X lido, imprima a
soma dos 5 pares consecutivos a partir de X
inclusive o X , se for par.
Se o valor de entrada for 4, por exemplo
a saída deve ser 40, que é o resultado
da operação: 4+6+8+10+12, enquanto que se
o valor de entrada for 11, por exempo,
a saída deve ser 80, que é a soma de 12+14+16+18+20.'''

# Atribui um valor alto para x
x = 999

# Laço para verificar se x é diferente de 0, se for true ele entra
while x != 0:
    # Le um valor de entrada
    x = int(input())
    # Cria a variável soma com valor 0
    soma = 0
    # Cria a variavel i com valor 1
    i = 1
    # Entra no for quando x for diferente de 0
    if x != 0:
        # Laço que se repete enquanto i for menor ou igual a 5
        while i <= 5:
            # For com a logica para saber se x é par e fazer a soma dos valores
            if x % 2 == 0:
                soma = soma + x
                x = x + 1
                i = i+ 1
            else:
                x = x + 1          
        # Mostra na tela o resultado da soma   
        print(soma)
    # Condição para para a execução
    elif x ==0:
        break
