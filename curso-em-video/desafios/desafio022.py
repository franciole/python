print("""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.""")
nome = str(input('Qual o seu nome completo: ')).strip()
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras desconsiderando os espaços.'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome tem  {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O primeiro nome é {} tem {} letras'.format(separa[0], len(separa[0])))
print('Finalizado OK')
