print('Exercício Python 020: O mesmo professor do desafio 019 \n'
      'quer sortear a ordem de apresentação de trabalhos dos alunos. \n'
      'Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
import random
a1 = input('Nome do 1º aluno: ')
a2 = input('Nome do 2º aluno: ')
a3 = input('Nome do 3º aluno: ')
a4 = input('Nome do 4º aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('Os nomes dos alunos para o sorteio foram\n'
      '1º {} \n'
      '2º {} \n'
      '3º {} \n'
      '4º {} \n'
      'A ordem dos alunos para apresentar o trabalho é conforme abaixo:\n'
      'Lista {}'.format(a1, a2, a3, a4, lista))

