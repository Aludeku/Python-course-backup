val = float(input('Qual é o preço do produto? R$'))
cinc = val*0.05
desc = val - cinc
print('O produto que custava R${:.2f}, na promoção de 5% de desconto vai custar R${:.2f}'.format(val,desc))