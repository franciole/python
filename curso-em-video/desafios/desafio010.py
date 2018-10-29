print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e '
      'mostre quantos dólares ela pode comprar.')
n = float(input('Qual o valor que você tem na carteira: R$ '))
d = 3.27
r = n / d
print('O valor do dólar atual é U${:.2f} \n'
      'Com R${:.2f} você pode comprar U${:.2f} de dólares '.format(d, n, r))
