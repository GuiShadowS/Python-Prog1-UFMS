# -*- coding: utf-8 -*-

"""
    Ano Bissexto ou Ano não Bissexto - 1279
    Ler indefinidamente números inteiros
    representando anos, até que EOF seja encontrado.
    Para cada ano lido, deve-se analisar e mostrar
    se o ano é bissexto, huluculu, bulukulu, ou um
    ano comum.
    Para controlar o tipo de ano, serão utilizadas
    variáveis booleanas bissexto, huluculu e bulukulu.
    Entre duas análises completas de um ano deve-se
    mostrar uma linha em branco.
"""
branco = False
while True:
    try:
        ano = int(input())
    except EOFError:
        break
    
    bissexto = False
    huluculu = False
    bulukulu = False
    
    if branco:
        print()
    else:
        branco = True
    
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        bissexto = True
        print("This is leap year.")
    if ano % 15 == 0:
        huluculu = True
        print("This is huluculu festival year.")
    if ano % 55 == 0 and bissexto:
        bulukulu = True
        print("This is bulukulu festival year.")
    if not bissexto and not huluculu and not bulukulu:
        print("This is an ordinary year.")
