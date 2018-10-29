print("""
Exercício Python 033: Faça um programa que leia três números e mostre qual é 
o maior e qual é o menor.
""")
a = int(input('Número 01: '))
b = int(input('Número 02: '))
c = int(input('Número 03: '))
# Analisando quem é o menor
menor = ('a = {}' .format(a))
if b < a and b < c:
    menor = ('b = {}' .format(b))
if c < a and c < b:
    menor = ('c = {}' .format(c))

# Analizando quem é o maior
maior = ('a = {}' .format(a))
if b > a and b > c:
    maior = ('b = {} ' .format(b))
if c > a and c > b:
    maior = ('c = {}' .format(c))

# Imprimindo os valores
print('O número menor entre a, b, c foi {} ' .format(menor))
print('O número maior entre a, b, c foi {} ' .format(maior))
