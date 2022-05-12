# -*- coding: utf-8 -*-

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
    agua = ((10 * 6.08) + (5 * 7.79) + (5 * 7.93) + (5 * 8.75) + (5 * 10.76) + (10 * 12.9) + ((x - 50) * 14.21))
    esgoto = ((10 * 4.26) + (5 * 5.45) + (5 * 5.55) + (5 * 6.13) + (5 * 7.53) + (10 * 9.03) + ((x - 50) * 9.95))  
        
elif x >= 31 and x <= 50:
    agua = ((10 * 6.08) + (5 * 7.79) + (5 * 7.93) + (5 * 8.75) + (5 * 10.76) + ((x - 30) * 12.9))
    esgoto = ((10 * 4.26) + (5 * 5.45) + (5 * 5.55) + (5 * 6.13) + (5 * 7.53) + ((x - 30)* 9.03))
           
elif x >= 26 and x <= 30:
    agua = ((10 * 6.08) + (5 * 7.79) + (5 * 7.93) + (5 * 8.75) + ((x - 25) * 10.76)) 
    esgoto = ((10 * 4.26) + (5 * 5.45) + (5 * 5.55) + (5 * 6.13) + ((x - 25) * 7.53))
           
elif x >= 21 and x <= 25:
    agua = ((10 * 6.08) + (5 * 7.79) + (5 * 7.93) + ((x - 20) * 8.75))
    esgoto = ((10 * 4.26) + (5 * 5.45) + (5 * 5.55) + ((x - 20) * 6.13))
           
elif x >= 16 and x <= 20:
    agua = ((10 * 6.08) + (5 * 7.79) + ((x - 15) * 7.93)) 
    esgoto = ((10 * 4.26) + (5 * 5.45) + ((x - 15) * 5.55))
        
elif x >= 11 and x <= 15:
    agua = ((10 * 6.08) + ((x - 10) * 7.79))
    esgoto = ((10 * 4.26) + ((x - 10) * 5.45))

else:
    agua = (x * 6.08) 
    esgoto = (x * 4.26)
    
# Após ja ter o valor de agua e esgoto, será calculado
# o valor total a ser pago, somando com a taxa fixa de R$15.05
soma = 15.05 + agua + esgoto
    
# Agora será exibido na tela os prints conforme solicitado no exercicio
# usando o "end" para concatenar as informações na mesma linha
print("Consumo:",x, end=" ")
print("metros cúbicos") 
print("Total a pagar: R$ 15.05 + R$ {0:.2f}".format(agua),end=" ")
print("+ R$ {0:.2f}".format(esgoto),end=" ")
print("= R$ {0:.2f}".format(soma))