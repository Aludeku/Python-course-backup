aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['status'] = 'aprovado'
elif 5 <= aluno['media'] <= 7:
    aluno['status'] = 'recuperação'
else:
    aluno['status'] = 'reprovado'
print('-=' * 20)
print(f'  -O nome é igual a {aluno["nome"]}.')
print(f'  -A média é igual à {aluno["media"]}.')
print(f'  -A situação de {aluno["nome"]} é de {aluno["status"]}.')
print('  -end.')