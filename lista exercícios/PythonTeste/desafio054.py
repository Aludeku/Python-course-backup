from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,7):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    anos = atual - nasc
    print('essa pessoa tem {} anos'.format(anos))
    if anos>=18:
        totmaior += 1
    else:
        totmenor += 1
print('tivemos {} pessoas maiores de idade e {} menores de idade'.format(totmaior, totmenor))