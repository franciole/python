n1 = int(input('Entre com um número: '))
n2 = int(input('Entre com outro número '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \no produto é {}, \na divisão é {:.2f}'.format(s, m, d), end =" >>>> ")
print('Divisão inteira é {}, e a potência é {}'.format(di, e))