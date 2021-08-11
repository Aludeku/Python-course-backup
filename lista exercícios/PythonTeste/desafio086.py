matriz = [[], [], []]
for z in range(0, 3):
    matriz[0].append(int(input(f"Digite um valor para [0,{z}]: ")))
for u in range (0, 3):
    matriz[1].append(int(input(f'Digite um valor para [1,{u}]: ')))
for d in range (0, 3):
    matriz[2].append(int(input(f'Digite um valor para [2,{d}]: ')))
print('-='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])