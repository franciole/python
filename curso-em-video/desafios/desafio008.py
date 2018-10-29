print('Escreva um programa que leia um valor em metros. E\n o exiba convertido em centimetros e milímetros')
n = int(input('Digite um valor em metros: '))
print('O valor em metros é {}'.format(n))
print('Em km é {}km\n'
      'em hm é {}hm\n'
      'em am é {}am\n'
      'em dm é {}dm\n'
      'em cm é {}cm\n'
      'em mm é {}mm'
      .format((n /1000), (n /100), (n /10), (n *10), (n*100), (n*1000)))
