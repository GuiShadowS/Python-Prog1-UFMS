# -*- coding: utf-8 -*-

"""
    2471 - Codificador de strings
    Seu programa deverá ler uma string S e um deslocamento
    inteiro D > 0. Então, deslocar o código ASCII, por D
    posições, de cada caracter de S e gerar
    um string codificada C. Tanto S quanto C podem ter apenas
    caracteres ASCII de códigos 32 a 126, de modo que um
    deslocamento que faça o código ultrapassar 126 deverá
    ser ajustado para o código correto correspondente
    a partir de 32. Uma codificação perfeita
    ocorre quando a quantidade de letras QLS da string S é a
    mesma que a quantidade de letras QLC da string codificada C.
    A saída do programa também mostra se a
    codificação foi perfeita ou não.

    Entrada:
    Em uma linha, leia uma string S, e na próxima linha leia
    um deslocamento inteiro D > 0. 
    
    Saída:
    Ao final, mostrar a string S em uma linha, seguida de um
    espaço e a QLS, e a string codificada C na próxima linha,
    seguida de um espaço e QLC. Na terceira linha de saída
    mostre "Codificação Perfeita!" ou "Codificação Não Perfeita!",
    caso QLS seja igual a QLC, ou diferente, respectivamente.
    
    Exemplos de entrada:          Exemplos de saída:
    Eu ouvi um zumbido!           Eu ouvi um zumbido! 15
    5                             Jz%tz{n%zr% zrgnit& 13
                                  Codificação Não Perfeita!
                                  
    Que barulho!                  Que barulho! 10
    3                             Txh#eduxokr$ 10
                                  Codificação Perfeita!
"""

"""
    A ideia geral é ler a string original com input() e
    armazená-la na variável original. A seguir, o
    deslocamento é lido na próxima linha, com input()
    e convertido para int, e armazenado em desl.
    Calcula-se o tamanho da string com len(original)
    e o armazena em n.
    Cria-se uma variável codificada com string vazia,
    para ir armazenando cada novo caracter gerado
    a partir da codificação.
    Para contabilizar a quantidade de letras da string
    original inicializa-se o contador letras_original
    com 0.
    Para contabilizar a quantidade de letras da string
    codificada inicializa-se o contador letras_codificada
    com 0.
    Utilizamos um laço for para acessar cada caracter
    da string original. No laço for, calculamos o código
    a ser colocado na string codificada, pela soma
    do código do caracter da string original, mais
    o deslocamento, fazendo resto da divisão inteira
    por 127. Caso o código gerado seja menor que
    32, somamos 32 para que os códigos fiquem sempre
    entre 32 e 126. Então concatenamos o caracter
    correspondente ao novo código na string codificada.
    Ainda no laço for, verificamos se o caracter da string
    original é uma letra (maiúscula ou minúscula) e
    contabilizamos em letras_original; e verificamos
    se o caracter da string codificada é uma letra
    (maiúscula ou minúscula) e contabilizamos em
    letras_codificada.
    Após o laço for é só mostrar a saída conforme
    solicitado.    
"""

# original = Ler a string original
original = input()

# desl = Ler o deslocamento
desl = int(input())

# n = Tamanho da string original
n = len(original)

# codificada = ""
codificada = ""

# letras_original = 0
letras_original = 0
# letras_codificada = 0
letras_codificada = 0

# para i de 0 a n-1
for i in range(n):
    # cod_orig = código do caracter original[i]
    cod_orig = ord(original[i])
    # A conta seguir gera um inteiro entre 0 e 126
    # cod_novo = (cod_orig+desl) % 127
    cod_novo = (cod_orig+desl) % 127
    # se cod_novo < 32
    if cod_novo < 32:
        # ajusta para ficar entre 32 e 126
        cod_novo += 32
    # codificada += caracter correspondente a cod_novo
    codificada += chr(cod_novo)
    # se cod_orig corresponde a uma letra maiúscula
    # ou minúscula
    if (cod_orig >= 65 and cod_orig <= 90) or\
       (cod_orig >= 97 and cod_orig <= 122):
        # letras_original += 1
        letras_original += 1
    # se cod_novo corresponde a uma letra maiúscula
    # ou minúscula
    if (cod_novo >= 65 and cod_novo <= 90) or\
       (cod_novo >= 97 and cod_novo <= 122):
        # letras_codificada += 1
        letras_codificada += 1    

# Mostrar a string original espaço letras_original
print(original, letras_original)

# Mostrar a string codificada espaço letras_codificada
print(codificada, letras_codificada)

# se letras_original == letras_codificada
if letras_original == letras_codificada:
    # Mostrar "Codificação Perfeita!"
    print("Codificação Perfeita!")
# senão
else:
    # Mostrar "Codificação Não Perfeita!"
    print("Codificação Não Perfeita!")
