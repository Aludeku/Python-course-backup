while True:
    n = int(input('\033[36mDigite um número para saber sua tabuada\033[m (\033[31mnegativo para parar o programa\033[m): '))
    if n < 0:
        break
    for c in range (1,11):
        mult = n * c
        print(f'{n} x {c} = {mult}')
print('Obrigado por usar!')