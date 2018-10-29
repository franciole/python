print("""
Exercício Python 028: Escreva um programa que faça o computador "pensar" em 
um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi 
o número escolhido pelo computador. O programa deverá escrever na tela se o 
usuário venceu ou perdeu.
""")
from random import randint
from time import sleep
linha = '-=-' * 30
computador = randint(0, 5)
print(linha)
print('O Camputador está pensando num número entre de 0 a 5 tente adivinhar...')
print(linha)
jogador = int(input('Digite um número entre 0 e 5: '))
print(linha)
print('PROCESSANDO...')
sleep(4)
if jogador == computador:
    print('Você ganhou, venceu o computador!')
else:
    print('Você perdeu eu pensei no número {} e você no número {}!'.format(computador, jogador))
print(linha)
print('Finalizado')