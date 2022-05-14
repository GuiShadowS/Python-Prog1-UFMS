# -*- coding: utf-8 -*-

'''
Vamos receber um numero do usuário que seja positivo e menor que 10000
e após isso mostrar a quantidade de milhar, dezena e centena que existe no numero
'''

# Le o numero inteiro menor que 10000 ja convertendo para inteiro
N = int(input())

# Para saber a milhar pegamos o numero e dividimos por 1000 e ficamos só com a parte inteira
milhar = N // 1000

# Para saber a centena pegamos o resto da divisão por 1000 e pegamos o valora da divisão inteira dele por 100
centena = (N % 1000) // 100

# Para saber a dezena pegamos o resto da divisão por 1000, dividimos por 100 e pegamos o resto novamente e depois pegamos a divisão inteira dele por 10
dezena = ((N % 1000) % 100) // 10

# Para saber a unidade pegamos o resto da divisão por 1000, dividimos por 100 e pegamos o resto novamente e depois pegamos o resto da divisão por 10 e dividimos por 10 novamente para pegar o resto
unidade = (((N % 1000) % 100) % 10) % 10

# Exibe na tela a saída conforme solicitado pelo programa
print(N,end="")
print(":")
print(milhar,"milhar(es)")
print(centena,"centena(s)")
print(dezena,"dezena(s)")
print(unidade,"unidade(s)")