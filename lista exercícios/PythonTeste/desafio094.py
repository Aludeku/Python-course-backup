pessoa = {}
galera = []
mulheres = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        if pessoa['sexo'] in 'Ff':
            mulheres.append(pessoa['nome'])
        print('Erro! responda apenas com M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! responda apenas com S ou N.')
    if resp == 'N':
        break
media = soma / len(galera)
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadsatradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=', ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for a in galera:
    if a['idade'] >= media:
        print(f'nome = {a["nome"]}; sexo = {a["sexo"]}; idade = 43;')
print(f'<< ENCERRADO >>')