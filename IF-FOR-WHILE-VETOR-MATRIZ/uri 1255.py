# coding: utf-8
"""
Problema 1255 do URI - Frequência de Letras
Neste problema estamos interessados na frequência das
letras em uma dada linha de texto.

Especificamente, deseja-se saber qual(is) a(s) letra(s)
de maior frequência do texto, ignorando o “case sensitive”,
ou seja maiúsculas ou minúsculas (sendo mais claro,
“letras” referem-se precisamente às 26 letras do alfabeto).

Entrada:
A entrada contém vários casos de teste. A primeira
linha contém um inteiro N que indica a quantidade
de casos de teste. Cada caso de teste consiste de uma
única linha de texto. A linha pode conter caracteres
“não letras”, mas é garantido que tenha ao menos uma
letra e que tenha no máximo 200 caracteres no total.

Saída:
Para cada caso de teste, imprima uma linha contendo
a(s) letra(s) que mais ocorreu(ocorreram) no texto
em minúsculas (se houver empate, imprima as letras
em ordem alfabética).

Exemplo de entrada:
3
Computers account for only 5% of the country's commercial electricity consumption.
Input
frequency letters

Exemplo de saída:
co
inptu
e
"""

# Ler a quantidade casos de teste
N = int(input())

"""
Iremos converter cada caracter para minúsculo
de modo que teremos apenas que analisar 26
caracteres, com códigos ASCII de 97 a 122.
O código ASCII pode ser obtido para função
built-in ord() do Python, e a transformação
para minúsculo é realizado pela função
built-in lower() do Python.

Para economizar o tamanho do vetor contador
de frequência, iremos alocar apenas um vetor (lista)
de 26 posições uma para cada letra minúscula,
inicializando sempre cada posição com 0, para cada
texto lido.

O vetor contador então irá contar quantos a's existem
na posição 0, quantos b's na posição 1, e assim
por diante, até quantos z's na posição 25.

Para indexar corretamente no vetor contador, ao percorrer
cada posição do texto lido, precisamos
subtrair o código ASCII de cada caracter de texto, após
torná-la minúscula, por 97, que é
o código ASCII da letra a, e verificar se o valor
resultante está no intervalo de 0 a 25, que será
o intervalo válido do vetor contador de letras minúsculas.
Ao indexar, simplesmente incrementamos o valor armazenado
na posição de uma unidade, pois teremos visto mais um
caracter no texto correspondente àquela posição do vetor.

Após percorrer o texto e verificar as frequências,
percorremos o vetor contador para verificar qual a maior
frequência. Então percorremos novamente o vetor contador
para que mostremos a saída em ordem alfabética.
"""
# Laço para ler N casos de teste
for i in range(N):
    # Cria e inicializa o vetor contador
    contador = [0]*26
    # Lê o texto deste caso de teste
    texto = input()
    
    # Percorre cada caracter do texto e o
    # converte para minúsculo, e verifica
    # se está no intervalo ASCII de 97 (a)
    # a 122 (z).
    # Se estiver então subtrai de 97 para indexar
    # corretamente o vetor contador
    for j in range(len(texto)):
        minus = ord(texto[j].lower())
        if minus >= 97 and minus <= 122:
            contador[minus - 97] += 1
    
    # Encontra a letra de maior frequência
    maiorfreq = -1
    for j in range(26):
        if contador[j] > maiorfreq:
            maiorfreq = contador[j]
        
    # Percorre o vetor contador e mostra todas
    # as letras que possuem a mesma maior frequência
    for j in range(26):
        if (contador[j] == maiorfreq):
            print(chr(j+97), end="")
    print() # Pular de linha para atender o requisito de saída
    

