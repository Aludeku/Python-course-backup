valores = []
count = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    count += 1
    quest = str(input('Deseja continuar?[S/N] '))
    if quest in 'nN':
        break
print(f'{count} números foram digitados')
if 5 in valores:
    cinco = valores.index(5)
valores.sort(reverse=True)
print(f'A lista de valores digitados em ordem decrescente é: {valores}')
if 5 in valores:
    print(f'O valor 5 está na lista na posição {cinco+1}')
else:
    print('O valor 5 não está na lista')