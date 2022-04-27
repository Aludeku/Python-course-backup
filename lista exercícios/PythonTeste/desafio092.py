from datetime import date

dici = {}
dici['nome'] = str(input('Nome: '))
dici['idade'] = int(input('Ano de Nascimento: '))
idade = date.today().year - dici['idade']
dici['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dici['ctps'] != 0:
    dici['contrataçao'] = int(input('Ano de contratação: '))
    dici['salario'] = float(input('Salário: R$ '))
print(f' Nome tem o valor de {dici["nome"]}')
print(f' Idade tem o valor de {idade}')
print(f' Ctps tem o valor de {dici["ctps"]}')
if dici['ctps'] != 0:
    print(f' Contratação tem o valor de {dici["contrataçao"]}')
    print(f' Salário tem o valor {dici["salario"]}')
    print(f' Aposentadoria tem o valor de {dici["contrataçao"] + 35 - dici["idade"]}')