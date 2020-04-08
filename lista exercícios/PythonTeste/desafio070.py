sum = many1000 = cheapname = 0
print('-'*30)
print('MERCADO SILVA')
print('-'*30)
while True:
    name = str(input('Nome do Produto: '))
    price = float(input('Preço do Produto: '))
    if price >= 1000:
        many1000 += 1
    elif price <= price:
        cheapname = name
    sum += price
    print('-'*30)
    option = ' '
    while option not in 'SN':
        option = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if option in 'Nn':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total gasto será: R$ {sum:.2f}. \n{many1000} produtos custam mais de R$ 1000,00. \nO produto mais barato é {cheapname}')