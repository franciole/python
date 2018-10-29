print('Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por \n'
      'um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, \n'
      'sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
precoDia = 60
precoKm = 0.15
qtdKmRodado = float(input('Informe a quantidade de KM rodados: '))
qtdDiasAluguel = float(input('Infome a quantidade de dias alugados: '))
valorTotal = (qtdKmRodado * precoKm) + (qtdDiasAluguel * precoDia)
print('O carro foi alugado por {} dias e rodou {:.1f} km com o valor total de R$ {:.2f}.'
      .format(qtdDiasAluguel, qtdKmRodado, valorTotal))
