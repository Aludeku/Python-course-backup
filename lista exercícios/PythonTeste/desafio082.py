valores = []
while True:
    valores.append(input('Digite um número: '))
    quest = str(input('Deseja continuar?[S/N] '))
    if quest in 'nN':
        break
    elif quest not in 'nNsS':
        quest = str(input('Digite S ou N: '))

print(f'Os números digitados foram {valores}')