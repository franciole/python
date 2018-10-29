print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada')
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O número digitado foi {} \no seu dobro é {} \no seu triplo é {} \n'
      'e a raiz quadrada é {}'.format(n, d, t, r))
print('\nCom uma variável apenas')
print('O número digitado foi {} \no seu dobro é {} \no seu triplo é {} \n'
      'e a raiz quadrada é {}'.format(n, (n*2), (n*3), (n**(1/2))))

print('\nCom uma variável apenas com a função pow')
print('O número digitado foi {} \no seu dobro é {} \no seu triplo é {} \n'
      'e a raiz quadrada é {}'.format(n, (n*2), (n*3), pow(n, (1/2))))
