lista = [[], []]
valor = 0
for v in range(1, 8):
    valor = int(input(f'Digite o {v}o. valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-='*30)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')