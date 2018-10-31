print("""
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
de até 200Km e R$0,45 parta viagens mais longas.
""")
d = float(input('Qual a distância da viagem em km: '))
if d <= 200:
    print('Até 200km o preço é de  R$ {:.2f}'.format(d * 0.50))
else:
    print('Acima de 200km o preço é de R$ {:.2f}'.format(d * 0.45))
print('Finalizado')
