# -*- coding: utf-8 -*-

'''
Criação de função simples que retorna se um numero inteiro
é par ou ímpar
'''

# Criação da função e seus parametros
def par(x):
    # Variável que irá receber o inteiro digitado
    par = int(input("Digite um numero inteiro para saber se é par ou ímpar: "))
    # Lógica para saber se é par ou ímpar
    if par % 2 == 0:
        x = "É par"
    else:
        x = "É ímpar"
    # Retorno do resultado
    return x

# Declaração de variável a ser usada
x = 0

# Declaração da variável que receberá o resultado
resultado = par(x)

# Mostra na tela o resultado
print(resultado)