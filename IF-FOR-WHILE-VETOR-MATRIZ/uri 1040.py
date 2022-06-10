# -*- coding: utf-8 -*-
"""
Leia quatro números (N1, N2, N3, N4),
cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas
notas e mostre esta média acompanhada pela mensagem "Media: ".
Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.".
Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa
deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame
obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada
pela nota digitada. Recalcule a média (some a pontuação do exame com a média
anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado."
(caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.",
(caso a média tenha ficado 4.9 ou menos). Para estes dois casos
(aprovado ou reprovado após ter pego exame) apresente na última linha uma
mensagem "Media final: " seguido da média final para esse aluno.
"""

# Leia quatro números (N1, N2, N3, N4) na mesma linha, separados por espaço,
# cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
N1s, N2s, N3s, N4s = input().split()
N1 = float(N1s)
N2 = float(N2s)
N3 = float(N3s)
N4 = float(N4s)

# Calcule a média com pesos 2, 3, 4 e 1, respectivamente,
# para cada uma destas notas
# M = (N1*2 + N2*3 + N3*4 + N4)/10
M = (N1*2 + N2*3 + N3*4 + N4)/10

# Mostrar "Media: " seguido de valor M com uma casa decimal
print("Media: {0:.1f}".format(M))

# se M >= 7.0
if M >= 7.0:
    # então Mostrar "Aluno aprovado."
    print("Aluno aprovado.")
# senão se M < 5.0
elif M < 5.0:
    # então Mostrar "Aluno reprovado."
    print("Aluno reprovado.")
# senão
else:
    # Mostrar "Aluno em exame."
    print("Aluno em exame.")
    # exame = Ler a nota do Exame
    exame = float(input())
    # Mostrar "Nota do exame: " seguido do valor de exame com uma casa decimal
    print("Nota do exame: {0:.1f}".format(exame))
    # nova_media = (M + exame) / 2
    nova_media = (M + exame) / 2
    # se nova_media >= 5.0
    if nova_media >= 5.0:
        # então Mostrar "Aluno aprovado."
        print("Aluno aprovado.")
    else:
        # senão Mostrar "Aluno reprovado."
        print("Aluno reprovado.")
    # Mostrar "Media final: " seguido de nova_media com uma casa decimal
    print("Media final: {0:.1f}".format(nova_media))
