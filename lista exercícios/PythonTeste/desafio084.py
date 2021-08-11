temp = []
princ = []
count = 0
maior = menor = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    count += 1
    temp.append(float(input('Digite o peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    quest = str(input('Quer continuar? [S/N]'))
    if quest in 'nN':
        break
print(f'{count} pessoas foram cadastradas')
print(f'O menor peso foi de {menor}kg.', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
print(f'\nO maior peso foi de {maior}kg.', end=' ')
for c in princ:
    if c[1] == maior:
        print(f'{c[0]}', end=' ')
