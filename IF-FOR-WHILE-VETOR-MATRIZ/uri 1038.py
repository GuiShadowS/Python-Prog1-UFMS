# -*- coding: utf-8 -*-

'''Escreva um programa que leia o código de um item
e a quantidade deste item. A seguir, calcule e mostre
o valor da conta a pagar'''

'''codigo  especificação     preço
    1      cachorro quente   R$4.00
    2      x-salada          R$4.50
    3      x-bacon           R$5.00
    4      torrada simples   R$2.00
    5      refrigerante      R$1.50'''

# Leia dois valores inteiros referentes ao codigo do item acima
# e a quantidade do mesmo, na mesma linha separados por espaço
cods, quants = input().split()

# Converte os valores str em inteiro
cod = int(cods)
quant = int(quants)

# Verifica qual o codigo primeiro
# após isso efetua o calculo do valor a ser pago
# pegando a quantidade do produto e multiplicando pelo seu valor
if cod == 1:
    soma = quant * 4.00
elif cod == 2:
    soma = quant * 4.50
elif cod == 3:
    soma = quant * 5.00
elif cod == 4:
    soma = quant * 2.00
else:
    soma = quant * 1.50

# Mostra na tela o valor a ser pago
print ("Total: R$ %0.2f" %soma)