# -*- coding: utf-8 -*-

'''
Exemplo de função criada para calcular o salario de um funcionário levando em consideração 
as horas extras que sejam feitas, e o valor da taxa, ao final imprime na tela o resultado
'''

# Função criada para calcular o salario de um funcionario
# Aqui eu defino a função com o nome e os parametros
def calcular_pagamento(qtd_horas, valor_hora):
  # Agora eu recebo as informações de quantas horas foram trabalhadas
  # E qual é a taxa a ser cobrada
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  # Verifico se foram feitas horas extras, e com base no resultado
  # Entro no if ou else e faço o calculo
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  # Mostro o valor calculado  
  return salario

# Solicito ao funcionario a quantidade de horas trabalhadas
# E solicito a taxa a ser usada no calculo
str_horas= input('Digite as horas: ')
str_taxa=input('Digite a taxa: ')

# Aqui eu faço uma variável receber o resultado da função criada acima
# atribuo a função com seus paramentros a variável para armazenar o valor
total_salario = calcular_pagamento(str_horas,str_taxa)

# Mostro na tela o resultado
print('O valor de seus rendimentos é R$',total_salario)
