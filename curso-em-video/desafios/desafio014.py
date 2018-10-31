print('Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius \n'
      'e converta para graus Fahrenheit\n'
      'Formulas \n'
      '(C-0)/100-0 = (F-32) / (212-32)\n'
      'C/100 = F-32/180\n'
      'Simplificando, temos:\n'
      'De Celsius para Fahrenheit\n'
      'F = (1.8* C) + 32\n'
      'De Fahrenheit para Celsius\n'
      'C = (F-32)/1.8')
tc = float(input('Informe a temperatura em Celsius: '))
f = (1.8 * tc) + 32
print('A temperatura em Celsius {:.1f} Cº é igual a Fahrenheit {:.1f} Fº'.format(tc, f))
linha = "_" * 30
print(linha)
tf = float(input('Informe a temperatura em Fahrenheit: '))
c = (tf -32)/1.8
print('A temperatura em Fahrenheit {:.1f} Fº é igual a Celsius {:.1f} Cº'.format(tf, c))
