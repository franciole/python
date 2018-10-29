print('Faça um algoritmo que leia o salário de um funcionário e '
      'mostre seu novo salário, com 15% de aumento')
salario = float(input('Qual o salário do funcionário R$ '))
p = 15
aumento = (salario * p) / 100
novoSalario = salario + aumento
print('O funcionário que recebia R$ {:.2f}, com {}% '
      'de aumento passará a receber {:.2f}'.format(salario, p, novoSalario))