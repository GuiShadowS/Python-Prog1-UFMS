# -*- coding: utf-8 -*-

'''
Função que calcula o índice de massa corporal de uma pessoa
e mostra em que nível a mesma se encontra!
'''

# Definimos o nome da função e seus parametros
def imc(altura, peso):
    # Ler a altura e o peso um em cada linha e salvar nas suas respectivas variáveis em formato de ponto flutuante
    altura = float(input("Digite sua altura utilizando ponto ex:1.75: "))
    peso = float(input("Digite seu peso utilizando ponto ex:69.5: "))
    
    # Logica do imc consiste em multiplicar a altura ao quadrado e dividir o resultado pelo peso
    imc = peso / (altura * altura)
    
    # Logica de Ifs para verificar em qual situação se enquadra seu imc e mostrar na tela o resultado
    if imc < 18.5:
        print("Você está abaixo do peso!")
        print("Seu IMC é:")
    elif imc >= 18.5 and imc <= 24.9:
        print("Você está no peso ideal!")
        print("Seu IMC é:")
    elif imc > 24.9 and imc <= 29.9:
        print("Você está com sobrepeso!")
        print("Seu IMC é:")
    elif imc > 29.9 and imc <= 40.0:
        print("Você está obeso!")
        print("Seu IMC é:")
    else:
        print("Você está com obesidade grave!")
        print("Seu IMC é:")
    return imc
    
# Definição de variáveis com valor 0.0 em ponto flutuante para ser usada na chamada da função
altura = 0.0
peso = 0.0

# Aqui eu atribuo uma variável que vai receber o resultado da função acima
resultado = imc(altura, peso)

# Mostra na tela o resultado da função criada
print("%.2f" %resultado)