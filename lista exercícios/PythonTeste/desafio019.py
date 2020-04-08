from random import choice
aluno1=input('Informe o nome do primeiro aluno:')
aluno2=input('O nome do segundo aluno:')
aluno3=input('O nome do terceiro aluno:')
aluno4=input('O nome do quarto aluno:')
lista = [aluno1,aluno2,aluno3,aluno4]
sorteado = choice(lista)
print('O aluno sorteado foi',sorteado)