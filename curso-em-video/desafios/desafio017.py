print('Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto \n'
      'e do cateto adjacente de um triângulo retângulo. \n'
      'Calcule e mostre o comprimento da hipotenusa')
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)
linha = ('_' * 80)
print('Mode sem import')
print('O cateto oposto {:.2f} com o cateto adjacente {:.2f} tem a hipotenusa = {:.2f} '.format(co, ca, h))
print(linha)
print('Modo com import')
print('O cateto oposto {:.2f} com o cateto adjacente {:.2f} tem a hipotenusa = {:.2f}'.format(co, ca, hi))
