velocidade = float(input('De quantos quilometros é sua viagem? '))
if velocidade>80:
    print('Você está rapido pra caceta')
    multa = (velocidade-80)*7
    print('Você pagará uma multa de R${:.2f}'.format(multa))
else: print('Você está dentro dos limetes de velocidade, que bom;')
print('Tenha um bom dia e dirija com segurança!')