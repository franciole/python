print('Cores no terminal')
a = 'Cores no termnial'
print('Style')
print ('0 - Nome  / 1 - Bold / 4 - Underline / 7 - Negative ')
print('Text')
print('30 / 31 / 32 / 33 / 34 / 35 / 36 / 37')
print('Back')
print('30 / 31 / 32 / 33 / 34 / 35 / 36 / 37')
print('\033[0;30;31m{}\033[m' .format(a))
print('\033[0;30;32m{}\033[m' .format(a))
print('\033[0;30;33m{}\033[m' .format(a))
print('\033[0;30;34m{}\033[m' .format(a))
print('\033[0;30;35m{}\033[m' .format(a))
print('\033[0;30;36m{}\033[m' .format(a))
print('\033[0;30;37m{}\033[m' .format(a))
print("-="*30)
print('\033[0;31;30m{}\033[m' .format(a))
print('\033[0;32;30m{}\033[m' .format(a))
print('\033[0;33;30m{}\033[m' .format(a))
print('\033[0;34;30m{}\033[m' .format(a))
print('\033[0;35;30m{}\033[m' .format(a))
print('\033[0;36;30m{}\033[m' .format(a))
print('\033[1;36;30m{}\033[m' .format(a))

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[34;31m{}\033[m !!!' .format(a, b))

nome = 'Franciole'
cores = {
        'Limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoBranco':'\033[7;30m'
}
print('Prazer em conhecer, {}{}{}!!!' .format(cores['azul'], nome, cores['Limpa']))
