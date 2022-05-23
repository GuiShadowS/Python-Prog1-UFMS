# -*- coding: utf-8 -*-

'''Faça um algoritmo para ler um número indeterminado
de dados, contendo cada um, a idade de um indivíduo.
O último dado, que não entrará nos cálculos,
contém o valor de idade negativa. Calcular e imprimir
a idade média deste grupo de indivíduos.'''

# Declaração de variáveis que serão usadas para
# manipular os valores 
soma = 0
cont = 0

# Lê o valor fornecido pelo usuario
idade = int(input())

# Lógica para verificar se o valor é maior que zero
# em seguida realizar a logica para somar todas
# as idades maiores que zero recebidas
# e dividi-las pelo total de idades
# que foi sendo incrementado a cada input
# na variável cont e após isso realizar a média aritmética
while idade > 0:
    soma = soma + idade
    cont = cont + 1
    idade = int(input())   
   
media = soma / cont

# Mostrar na tela o resultado com duas casas decimais
print("%.2f" %media)
