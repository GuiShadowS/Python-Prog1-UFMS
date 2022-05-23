# -*- coding: utf-8 -*-

'''
Uma sentença é chamada de dançante se sua primeira letra
for maiúscula e cada letra subsequente for o oposto
da letra anterior. Espaços devem ser ignorados
ao determinar o case (minúsculo/maiúsculo) de uma letra.
Por exemplo, "A b Cd" é uma sentença dançante
porque a primeira letra ('A') é maiúscula, a próxima letra
('b') é minúscula, a próxima letra ('C') é maiúscula
e a próxima letra ('d') é minúscula.
'''

while True:
    try:
        entrada = input()
    except EOFError:  
        break
  
    para_MA = True 
    dancante = ""    
  
    for i in range(len(entrada)):     
        car = entrada[i]       
       
        if car == " ":           
            dancante = dancante + " "        
        elif ord(car) >= 65 and ord(car) <= 90: 
          
            if para_MA == True:                
                dancante = dancante + car           
            else:               
                dancante = dancante + chr(ord(car) + 32)           
            para_MA = not para_MA       
        else:           
            if para_MA == True:                
                dancante = dancante + chr(ord(car) - 32)            
            else:                
                dancante = dancante + car            
            para_MA = not para_MA
    
    print(dancante)