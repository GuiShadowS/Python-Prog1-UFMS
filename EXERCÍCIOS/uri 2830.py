"""
Problema 2830 - Copa do URI:
Entrada:
A entrada consiste de duas linhas. A primeira linha da
entrada contém um inteiro K (1 ≤ K ≤ 16) que indica a
posição de Mestre Kung na chave. A segunda linha da
entrada contém um inteiro L (1 ≤ L ≤ 16, K ≠ L) que
indica a posição de Mestre Lu na chave.

Saída:
Seu programa deve produzir uma linha contendo uma das
palavras seguintes, decidindo a fase em que vão se
enfrentar os jogadores Mestre Kung e Mestre Lu, se
eles chegarem a se enfrentar: oitavas, quartas,
semifinal ou final.
"""

"""
  A ideia é ir restringindo o espaço de comparações, desde
  as possibilidades de valores para a final, e então
  para a semifinal, para as quartas, e o que sobrar
  serão para as oitavas.
  O esquema gráfico dado no enunciado ajuda muito
  na resolução porque facilita a linha de raciocínio.
"""
K = int(input())
L = int(input())

if ((K <= 8 and L > 8) or (K > 8 and L <= 8)):
    print("final")
elif ((K <= 4 and L > 4) or (K > 4 and L <= 4)) \
     or ((K <= 12 and L > 12) or (K > 12 and L <= 12)):
    print("semifinal")
elif ((K <= 2 and L > 2) or (K > 2 and L <= 2)) \
     or ((K <= 6 and L > 6) or (K > 6 and L <= 6)) \
     or ((K <= 10 and L > 10) or (K > 10 and L <= 10)) \
     or ((K <= 14 and L > 14) or (K > 14 and L <= 14)):
    print("quartas")
else:
    print("oitavas")
