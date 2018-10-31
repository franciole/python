print("""
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário 
e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um 
aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
""")
salario = float(input('Qual o seu salário: R$ '))
print('Seu salário é R$ {:.2f}'.format(salario))
if salario <= 1250:
    aumento = salario * 0.15
    print('Aumento de 15% R$ {:.2f} salário atual R$ {:.2f}'.format(aumento, (salario + aumento)))
else:
    aumento = salario * 0.10
    print('Aumento de 10% R$ {:.2f} salário atual R$ {:.2f}'.format(aumento, (salario + aumento)))
