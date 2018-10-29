print('Exercício Python 016: Crie um programa que leia um número Real qualquer \n'
      'pelo teclado e mostre na tela a sua porção Inteira\n'
      'Exemplo: Digite um número: 6.127.\n'
      'O número 6.127 tem a parte inteira 6.')

from math import trunc
n = float(input('Informe um número qualquer: '))
linha = ('_' * 60)
print('Com import de trunc')
print('A parte inteira do número {} informado é {}'.format(n, trunc(n)))
print(linha)
print('Com o função int.')
print('A parte inteira do número {} informado é {}'.format(n, (int(n))))
print(linha)
