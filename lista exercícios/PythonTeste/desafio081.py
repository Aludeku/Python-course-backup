valores = []
count = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    count += 1
    quest = str(input('Deseja continuar?[S/N] '))
    if quest in 'nN':
        break
print(f'{count} números foram digitados')
print(f'A lista de valores digitados em ordem decrescente é: {valores.sort(reverse=True)}')
if 5 in valores:
    print(f'O valor 5 está na lista na posição {valores.index(5(valores))}')
else:
    print('O valor 5 não está na lista')