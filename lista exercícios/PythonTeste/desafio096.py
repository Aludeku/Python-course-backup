print('Controle de Terrenos')
print('-' * 20)


def area(lar, com):
    are = lar * com
    print(f'A área de um terreno {lar}x{com} é de {are}m².')


area(
    lar = float(input('Largura (m): ')),
    com = float(input('Comprimento (m): '))
)
