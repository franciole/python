print("""Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou 
        não com o nome "SANTO".""")
cidade = str(input('Qual o nome da sua cidade: ')).strip()
print('O nome da cidade que você nasceu é {} - {}'.format(cidade, cidade[:5].upper() == 'SANTO'))
print('Finalizado')
