print("""
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.
""")
velocidade = float(input('Qual a velocidade do carro em km/h: '))
if velocidade > 80:
    print('Você foi multado ultrapassou o limite de velocidade de 80km/h')
    multa = (velocidade - 80) * 7
    print('O valor da multa é de R$ {:.2f}'.format(multa))
print('Tenha um bom dia diriga com segurança!')
print('Finalizado')