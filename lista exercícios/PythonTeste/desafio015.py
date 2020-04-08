dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
preço = 60*dias + 0.15*km
print('O total a pagar é \033[32mR${:.2f}'.format(preço))