valores = []
while True:
    adc = (int(input('Digite um valor: ')))
    if adc not in valores:
        valores.append(adc)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    continuar = (str(input('Quer continuar?[S/N] ')))
    if continuar in 'nN':
        break
print(f'Você digitou os valores {sorted(valores)}')