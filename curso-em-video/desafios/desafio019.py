print('Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. \n'
      'Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.')
import random
a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('Os nomes dos alunos para o sorteio foram\n'
      '1º {} \n'
      '2º {} \n'
      '3º {} \n'
      '4º {} \n'
      'O aluno que foi sorteado para apagar o quadro foi {}'.format(a1, a2, a3, a4, sorteio))
