nota1 = float(input('Quanto você tirou na primeira prova? '))
nota2 = float(input('Quanto você tirou na segunda prova?'))
media = (nota1+nota2)/2
print('Sua média é de {:.1f}'.format(media))
if media<5.0:
    print('\033[31mREPROVADO\033[m')
elif media >= 5 and media<7:
    print('\033[33mRECUPERAÇÃO\033[m')
elif media>6.9:
    print('\033[32mAPROVADO\033[m')