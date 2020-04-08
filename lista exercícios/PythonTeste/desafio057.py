print('-'*12, 'INFORMADOR DE SEXO', '-'*12)
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Incorreto, informe novamente [M/F]: '))
if sexo == 'M':
    sexo = 'masculino'
elif sexo == 'F':
    sexo = 'feminino'

print('O sexo informado foi {}'.format(sexo))