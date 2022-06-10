# -*- coding: utf-8 -*-

"""
    Relógio Antigo - 3084
    Ler pares de ângulos dos ponteiros das horas e dos minutos,
    até que seja gerado EOFError.
    A cada par de ângulos, calcula-se a quantidade de horas
    e minutos conforme as fórmulas a seguir:
    horas = (ângulo do ponteiro das horas) / 30
    minutos = (ângulo do ponteiro dos minutos) / 6
    Mostrar horas:minutos, com dois dígitos nas horas
    e minutos, colocando-se 0 à esquerda caso o valor
    de hora ou minuto seja menor do que 10.
"""

# Enquanto Verdadeiro
while True:
    try:
        # angh, angm = Ler ângulos de horas e minutos
        anghs, angms = input().split()
    except EOFError:
    # se ocorrer EOFError
        # então Sair do laço enquanto
        break
    angh = int(anghs)
    angm = int(angms)
    # horas = angh // 30
    horas = angh // 30
    # minutos = angm // 6
    minutos = angm // 6
    # Mostrar horas:minutos, com dois dígitos nas horas
    # e minutos, colocando-se 0 à esquerda caso o valor
    # de hora ou minuto seja menor do que 10
    print("{0:02d}:{1:02d}".format(horas, minutos))
