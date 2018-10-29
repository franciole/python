print('Exercício Python 018: Faça um programa que leia um ângulo qualquer \n'
      'e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
from math import sin, cos, tan, radians
a = float(input('Informe um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('Para o âmgulo {}º informamo temos abaixo:\n'
      'Seno {:.4f}\n'
      'Cosseno {:.4f}\n'
      'Tangente {:.4f}'.format(a, s, c, t))
