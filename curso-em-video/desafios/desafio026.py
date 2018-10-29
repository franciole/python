print("""Exercício Python 026: Faça um programa que leia uma frase pelo teclado e 
        mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira 
        vez e em que posição ela aparece a última vez.""")
frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('A frase digitada foi {} e tem {} letra A.'.format(frase, frase.count('A')))
print('Aparece na primeira vez em {}'.format(frase.find('A')+1))
print('Aparece na última posição {}'.format(frase.rfind('A')+1))
print('Finalizado')