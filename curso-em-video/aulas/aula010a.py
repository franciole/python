nome = str(input('Qual o seu nome: '))
if nome == 'Franciole' :
    print('Que nome lindo você tem!')
print('Bom dia, {}"'.format(nome))
linha = '-=-' * 15
print(linha)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) /2
print('A sua média foi {:.1f} '.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print(linha)
print('Condição Simplificada.')
print('PARABÉNS' if m >= 6.0 else 'ESTUDE MAIS')
print(linha)
print('FIM')

