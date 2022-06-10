# -*- coding: utf-8 -*-

'''
Sheldon Cooper é um personagem excêntrico existente no universo de Hollywood. Recentemente ele sofreu um acidente e acabou esquecendo quais frutas gosta de comer. 
Contudo, é chegada a hora de preparar o café da manhã e Sheldon não quer passar pela experiência de provar uma fruta e descobrir que não gosta dela. Então, 
incomodado com essa situação, Sheldon convenceu seu amigo Leonard Hofstadter a lhe ajudar. Leonard lembra do momento que conheceu Sheldon e devido as 
excentricidades de seu amigo, ele guardou em seu computador uma lista com o nome das frutas que Sheldon gosta de comer. Leonard muito animado com sua sagacidade, 
abre o arquivo e observa que algo está errado: o conteúdo do arquivo foi embaralhado por um vírus de computador.

Determinado a resolve essa questão, Leonard fez experimentos e concluiu que é possível ler o conteúdo do arquivo e descobrir se Sheldon gosta ou não de uma dada fruta. 
Pelos experimentos, Leonard observou que o vírus fez alguma(s) das seguintes alterações: 1) Incluiu novos caracteres à esquerda e/ou à direita ao nome da fruta 
que estava na lista; 2) Alterou algumas letras, neste caso, algumas se tornaram maiúsculas e outras minúsculas; 3) O nome da fruta que estava na lista foi invertido
 ("Bergamota" => "Atomagreb"). Como Leonard estudou programação, ele irá criar um programa que recebe o nome de uma fruta e retorna se Sheldon gosta ou não dessa fruta.
'''

# m, n = Ler os dois inteiros em uma mesma linha
linha = input().split()
m = int(linha[0])
n = int(linha[1])

# Criar vetor para as frutas
# vf = m*[""]
vf = m*[""]

# Criar vetor para as linhas codificadas
# vc = n*[""]
vc = n*[""]

# para i de 0 até m-1
for i in range(m):
    # vf[i] = para_minúsculo(Ler string de entrada)
    vf[i] = input().lower()

# para i de 0 até n-1
for i in range(n):
    # vc[i] = para_minúsculo(Ler string de entrada)
    vc[i] = input().lower()

# para fruta EM vf # ALTERNATIVA
# para i de 0 até m-1
for i in range(m):
    # fruta = vf[i]
    fruta = vf[i]
    # fruta_inv = inverso(fruta)
    fruta_inv = fruta[::-1]
    
    # achou = Falso
    achou = False
    # para j de 0 até n-1
    for j in range(n):
        # se fruta EM vc[j] OU fruta_inv EM vc[j]
        if fruta in vc[j] or fruta_inv in vc[j]:
            # achou = Verdadeiro
            achou = True
            # Sair do laço para
            break
    # se achou
    if achou: # if achou == True:
        # Mostrar "Sheldon come a fruta "fruta
        print("Sheldon come a fruta", fruta)
    # senão
    else:
        # Mostrar "Sheldon detesta a fruta "fruta
        print("Sheldon detesta a fruta", fruta)