valores = []
for v in range(0,5):
    adc = (int(input('Digite um valor: ')))
    if v == 0 or adc > valores[-1]:
        valores.append(adc)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if adc <= valores[pos]:
                valores.insert(pos, adc)
                print(f'Valor {adc} adicionado na posição {pos}')
                break
            pos += 1

print(f'Você digitou os valores {valores}')