print("""
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e 
diga ao usuário se elas podem ou não formar um triângulo.
""")
linha = ('-=' * 20)
print(linha)
print('Analizando de triângulas')
print(linha)
s1 = float(input('Informe o primeiro segmento: '))
s2 = float(input('Infomre o segundo segmento: '))
s3 = float(input('Informe o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos informados acima PODEM formar um triângulo.')
else :
    print('Os segmentos informados acima NÂO PODEM formar um triângulo.')
