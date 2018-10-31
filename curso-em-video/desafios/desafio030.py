print("""
Exercício Python 030: Crie um programa que leia um número inteiro e mostre 
na tela se ele é PAR ou ÍMPAR.
""")
n = int(input('Informe um número inteiro: '))
r = n % 2
if r == 0:
    print('Número par!')
else:
    print('Número ímpar!')

print('Finalizado')
