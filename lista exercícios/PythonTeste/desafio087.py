matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
ter = pares = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz [l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print('=-' * 30)
print(f'A soma dos números pares é {pares}')
for t in range(0, 3):
    ter += matriz[t][2]
for m in range(0, 3):
    if mai == 0:
        mai = matriz[1][0]
    else:
        if matriz[1][m] >= mai:
            mai = matriz[1][m]
print(f'A soma de valores da terceira coluna é {ter}')
print(f'O maior valor da segunda linha é {mai}')