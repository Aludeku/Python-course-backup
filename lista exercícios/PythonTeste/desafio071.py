print('\033[30;45m BANCO \033[m')
print('-_'*15)
value = int(input('Quanto você deseja sacar? R$ '))
while True:
    if value == 0:
        break
    fifty = int(value /50)
    print('{} notas de R$50,00 reais'.format(fifty))
    value = value %50
    if value %50 != 0:
        twenty = int(value /20)
        print('{} notas de R$20,00 reais'.format(twenty))
        value = value %20
        if value %20 != 0:
            ten = int(value /10)
            print('{} notas de R$10,00 reais'.format(ten))
            value = value %10
            if value %10 != 0:
                five = int(value /5)
                print('{} notas de R$5,00 reais'.format((five)))
                if value %5  != 0:
                    one = int(value/1)
                    print(f'{one} notas de R$1,00 real.')
                    value = value %1
print('\033[35mEsse foi dificil! \033[m')