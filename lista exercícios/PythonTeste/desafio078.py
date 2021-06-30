valores = []
for v in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
print('-='*40)
print(f'Sua lista de valores é {valores}')
print(f'O maior valor digitado foi {max(valores)} na posição {(valores.index(max(valores)))}')
print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')

