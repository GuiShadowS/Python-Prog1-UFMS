# -*- coding: utf-8 -*-

'''
O programa receberá 5 códigos de cursos da FACOM do instituto de MAtemática
INMA e de outras unidades, com isso o programa deve contabilizar quantos códigos pertencem a cursos da FACOM
quantos códigos são cursos do INMA e o resto entra como curso de outras unidades
'''

# Leia 5 numeros inteiros separados por espaço
N1, N2, N3, N4, N5 = input().split()

# Converte e atribui a cada variável seu valor
N1 = int(N1)
N2 = int(N2)
N3 = int(N3)
N4 = int(N4)
N5 = int(N5)

# declarar um contador para fazer a soma
contadorfacom = 0
contadorinma = 0
outros = 0

# Fazer comparação dos valores e caso sejam True adicionar +1 ao contador
if N1 == 1902 or N1 == 1904 or N1 == 1905 or N1 == 1906 or N1 == 1907:
    contadorfacom = contadorfacom + 1
elif N1 == 2201 or N1 == 2202 or N1 == 2203 or N1 == 1906 or N1 == 2291:
    contadorinma = contadorinma + 1
else:
    outros = outros + 1


if N2 == 1902 or N2 == 1904 or N2 == 1905 or N2 == 1906 or N2 == 1907:
    contadorfacom = contadorfacom + 1
elif N2 == 2201 or N2 == 2202 or N2 == 2203 or N2 == 1906 or N2 == 2291:
    contadorinma = contadorinma + 1
else:
    outros = outros + 1


if N3 == 1902 or N3 == 1904 or N3 == 1905 or N3 == 1906 or N3 == 1907:
    contadorfacom = contadorfacom + 1
elif N3 == 2201 or N3 == 2202 or N3 == 2203 or N3 == 1906 or N3 == 2291:
    contadorinma = contadorinma + 1
else:
    outros = outros + 1


if N4 == 1902 or N4 == 1904 or N4 == 1905 or N4 == 1906 or N4 == 1907:
    contadorfacom = contadorfacom + 1
elif N4 == 2201 or N4 == 2202 or N4 == 2203 or N4 == 1906 or N4 == 2291:
    contadorinma = contadorinma + 1
else:
    outros = outros + 1


if N5 == 1902 or N5 == 1904 or N5 == 1905 or N5 == 1906 or N5 == 1907:
    contadorfacom = contadorfacom + 1
elif N5 == 2201 or N5 == 2202 or N5 == 2203 or N5 == 1906 or N5 == 2291:
    contadorinma = contadorinma + 1
else:
    outros = outros + 1
    
    
# Mostre o resultado de quantos estudantes
# fazem parte das unidades facom, inma ou outras unidades
print("Facom:", contadorfacom)
print("Inma:", contadorinma)
print("Outras unidades:", outros)