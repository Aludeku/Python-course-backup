lista = []
for c in range(1, 8):
    lista.append(int(input(f'Digite o {c}o. valor: ')))
print('-='*30)
pares = []
impares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f'Os valores pares digitados foram: {sorted(pares)}')
print(f'Os valores ímpares digitados foram: {sorted(impares)}')