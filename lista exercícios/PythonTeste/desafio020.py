from random import shuffle
n1 = str(input('O nome do primeiro aluno: '))
n2 = str(input('O nome do segundo aluno: '))
n3 = str(input('O nome do terceiro aluno: '))
n4 = str(input('O nome do quarto aluno: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem definida foi:')
print(lista)