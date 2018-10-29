from datetime import  date
print("""
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
""")
ano = int(input('Digite um ano para saber se é bissexto para o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.' .format(ano))
else:
    print('O ano {} não é bissexto.' .format(ano))
