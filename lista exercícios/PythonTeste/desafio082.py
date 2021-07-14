valores = []
impares = []
pares = []
while True:
    valores.append(int(input('Digite um número: ')))
    quest = str(input('Deseja continuar?[S/N] '))
    if quest in 'nN':
        break
    elif quest not in 'nNsS':
        quest = str(input('Digite S ou N: '))
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Os números pares digitados foram {pares}')
print(f'Os números ímpares digitados foram {impares}')
print(f'Os números digitados foram {valores}')