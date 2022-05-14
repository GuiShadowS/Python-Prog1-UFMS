# -*- coding: utf-8 -*-

'''
Programa vai calcular a média de aproveitamento de uma disciplina
levando em conta as notas da P1, P2 e P3 mais o trabalho pratico TP
MA = (80% da média de P1, P2 e P3) + (20% da nota do trabalho prático).
caso a nota da media seja menor que 6, deve-se substituir a menor nota entre
as provas pela nota da p.o e refazer o calculo, caso a media final seja
maior ou igual a 6 o aluno está aprovado, caso contrario estará reprovado.
'''

# Entrada das notas pelo usuário, na mesma linha
p1s, p2s, p3s, tps = input().split()

# Conversão dos valores str para float
p1 = float(p1s)
p2 = float(p2s)
p3 = float(p3s)
tp = float(tps)

# Cálculo da média de aproveitamento
ma = (((p1 + p2 + p3) / 3) * 0.80) + (tp * 0.20)


# Se a média foi maior ou igual a 6 o programa imprime a media na tela
# e na linha abaixo a frase "Estudante aprovado(a)" e encerra
if ma >= 6:
    print("MA: %.1f"% ma)
    print("Estudante aprovado(a)")

# Caso a média seja menor que 6, mostra a mensagem "O(A) estudante precisa fazer a prova optativa!"
else:
    print("O(A) estudante precisa fazer a prova optativa!")
    opt = float(input())
    # Esse bloco de if verifica qual a menor nota entre P1, P2, P3 e a subistitui pela nota da P.O
    if opt < p1 and opt < p2 and opt < p3:
        p1 = p1
        p2 = p2
        p3 = p3
    elif p1 < p2 and p1 < p3:
        p1 = opt
    elif p2 < p1 and p2 < p3:
        p2 = opt
    else:
        p3 = opt

    # O calculo da média é refeito agora com a nota da P.O subistituindo a menor nota
    ma = (((p1 + p2 + p3) / 3) * 0.80) + (tp * 0.20)

    # Nesse bloco de if é verificado se a nova média foi maior ou menor que 6 e mostra na tela a mensagem correspondente
    if ma < 6:
        print("MA: %.1f"% ma)
        print("Estudante reprovado(a)")
    else:
        print("MA: %.1f"% ma)
        print("Estudante aprovado(a)")