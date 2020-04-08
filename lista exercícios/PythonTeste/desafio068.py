from random import randint
count = 0
bot = randint(1,10)
print('\033[33mÍmpar ou Par\033[m')
print('=-'*15)
while True:
    n = int(input('\033[35mDigite um número: '))
    opt = ' '
    while opt not in 'PpIi':
        opt = str(input('Escolha Ímpar ou Par [I/P]:\033[m ')).strip().upper()[0]
    print('-'*30)
    sum = n + bot
    print(f'Você digitou {n} e o computador {bot}. Total de {sum} ', end='')
    if sum % 2 :
        print('deu ímpar')
        if opt in 'Ii':
            print('-'*15)
            print('\033[32mVocê venceu\033[m')
            count += 1
        else:
            print('-'*15)
            print('\033[31mVocê perdeu\033[m')
            break
    else:
        print('deu par')
        if opt in 'Pp':
            print('-' * 15)
            print('\033[32mVocê venceu\033[m')
            count += 1
        else:
            print('-' * 15)
            print('\033[31mVocê perdeu\033[m')
            break
print('\033[31m-\033[m'*30)
print(f'\033[31mGAME OVER!\033[m você venceu \033[35m{count}\033[m vezes.')