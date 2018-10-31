print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço\n'
      'Com 5% de desconto')
n = float(input('Qual o preço do produto: R$ '))
p = 5
d = (n * p) / 100
res = n - d
print('O produto de R$ {:.2f} com desconto de {}% = R$ {:.2f} ficará em R$ {:.2f}'.format(n, p, d, res))
