print('CADASTRO DE PESSOAS')
#count18 = people over 18yo, man = man, wom20 = woman below 20yo
count18 = man = wom20 = 0
while True:
    print('--'*15)
    age = int(input('Idade: '))
    if age >= 18:
        count18 += 1
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sex in 'Mm':
        man += 1
    elif age < 20 and sex in "Ff":
        wom20 += 1
    opt = str(input('Quer continuar? [S/N] '))
    if opt in 'nN':
        break
print('--'*15)
print('FIM DO PROGRAMA!')
print(f'Total de pessoas com mais de 18 anos: {count18}.')
print(f'Ao todo {man} homens cadastrados.')
print(f'E {wom20} mulheres com menos de 20 anos.')