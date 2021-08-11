matriz = [[], [], []]
pares = []
for z in range(0, 3):
    matriz[0].append(int(input(f"Digite um valor para [0,{z}]: ")))
for p in matriz:
    if matriz[0][p] % 2 == 0:
        pares.append(matriz[0][p])
for u in range (0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1,{u}]: ')))
    maior = matriz[1][0]
if matriz[1][1] > maior:
    maior = matriz[1][1]
else:
    if matriz[1][2] > matriz[1][1]:
        maior = matriz[1][2]
for d in range (0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2,{d}]: ')))
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'Todos os valores pares digitados foram: {pares}')
print(f'A soma de valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {maior}')