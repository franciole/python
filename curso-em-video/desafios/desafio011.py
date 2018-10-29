print('Faça um programa que leia a largura e a altura de uma parede em metros.\n'
      'Calcule a sua área e a quantidade de tinta necessária para pintá-la.\n'
      'Sabendo que cada litro de tinta pinta uma área de 2m2')
larg = float(input('Qual a larugura da parede: '))
alt = float(input('Qual a altura da parede: '))
area = larg * alt
areaPintura = 2
tinta = area / areaPintura
print('A area total da parede é {} \n'
      'Para pintar essa parede, você precisar de {} litros de tinta.'.format(area, tinta))
