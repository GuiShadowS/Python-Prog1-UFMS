# -*- coding: utf-8 -*-

'''
Esse programa vai receber um valor inteiro que corresponde a quantos metros cubicos de agua uma pessoas gastou e com base na tabela abaixo ele irá decompor o valor e efetuar os calculos
após o encaixar o valor em uma linha de calculo, ele tambem deve calcular as linhas anteriores até o começo no 1 a 10m3

Por exemplo, para 18 m³, deve-se calcular o valor total computando o custo por unidade de consumo de cada faixa:
15.05 + (10*6.08 + 5*7.79 + 3*7.93) + (10*4.26 + 5*5.45 + 3*5.55) =
15.05 + 123.54 + 86.50 = 225.09

Tarifa Fixa R$ 15,05

Consumo Residencial   Água (R$/m³)  Esgoto (R$/m³)

1 a 10 m³             6,08          4,26

11 a 15 m³            7,79          5,45

16 a 20 m³            7,93          5,55

21 a 25 m³            8,75          6,13

26 a 30 m³           10,76          7,53

31 a 50 m³           12,9           9,03

Acima 50 m³          14,21          9,95
'''

# Leia um numero inteiro <= 0
x = int(input())

# Declaraçaõ de variáveis que serão usadas nos calculos a seguir
soma = 0
agua = 0
esgoto = 0

# Com o valor informado pelo usuário os calculos abaixo serão feitos
# para a agua e esgoto, usando uma estrutura de if e elif para comparar 
# o valor recebido e verificar em qual situação ele se encaixa
if x > 50:
    agua = ((10 * 6.08) + (5 * 7.79) + (5 * 7.93) + (5 * 8.75) + (5 * 10.76) + (20 * 12.9) + ((x - 50) * 14.21))
    esgoto = ((10 * 4.26) + (5 * 5.45) + (5 * 5.55) + (5 * 6.13) + (5 * 7.53) + (20 * 9.03) + ((x - 50) * 9.95))
    soma = 15.05 + agua + esgoto
        
elif x >= 31 and x <= 50:
    agua = ((10 * 6.08) + (5 * 7.79) + (5 * 7.93) + (5 * 8.75) + (5 * 10.76) + ((x - 30) * 12.9))
    esgoto = ((10 * 4.26) + (5 * 5.45) + (5 * 5.55) + (5 * 6.13) + (5 * 7.53) + ((x - 30)* 9.03))
    soma = 15.05 + agua + esgoto
           
elif x >= 26 and x <= 30:
    agua = ((10 * 6.08) + (5 * 7.79) + (5 * 7.93) + (5 * 8.75) + ((x - 25) * 10.76)) 
    esgoto = ((10 * 4.26) + (5 * 5.45) + (5 * 5.55) + (5 * 6.13) + ((x - 25) * 7.53))
    soma = 15.05 + agua + esgoto
           
elif x >= 21 and x <= 25:
    agua = ((10 * 6.08) + (5 * 7.79) + (5 * 7.93) + ((x - 20) * 8.75))
    esgoto = ((10 * 4.26) + (5 * 5.45) + (5 * 5.55) + ((x - 20) * 6.13))
    soma = 15.05 + agua + esgoto
           
elif x >= 16 and x <= 20:
    agua = ((10 * 6.08) + (5 * 7.79) + ((x - 15) * 7.93)) 
    esgoto = ((10 * 4.26) + (5 * 5.45) + ((x - 15) * 5.55))
    soma = 15.05 + agua + esgoto
        
elif x >= 11 and x <= 15:
    agua = ((10 * 6.08) + ((x - 10) * 7.79))
    esgoto = ((10 * 4.26) + ((x - 10) * 5.45))
    soma = 15.05 + agua + esgoto

elif x >= 1 and x <= 10:
    agua = (x * 6.08) 
    esgoto = (x * 4.26)
    soma = 15.05 + agua + esgoto
    
else:
    soma = 15.05
        
# Agora será exibido na tela os prints conforme solicitado no exercicio
# usando o "end" para concatenar as informações na mesma linha
print("Consumo:",x,"metros cúbicos") 
print("Total a pagar: R$ 15.05 + R$ {0:.2f}".format(agua),end=" ")
print("+ R$ {0:.2f}".format(esgoto),end=" ")
print("= R$ {0:.2f}".format(soma))