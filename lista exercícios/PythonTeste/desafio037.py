num = int(input('\033[36mDigite um número inteiro:\033[m '))

decidir = int(input(
    '\033[36mEscolha qual será a base de conversão:\033[m \n\033[31mdigite [1] para binário\033[m\n\033[32mdigite [2] para octal\033[m\n\033[34mdigite [3] para hexadecimal:\033[m '))
if decidir == 1:
    print('\033[31mconvertendo {} para binário fica:\033[m {}'.format(num, bin(num)))
elif decidir == 2:
    print('\033[32mconvertendo {} para octal fica:\033[m {}'.format(num, oct(num)))
elif decidir == 3:
    print('\033[34mconvertendo {} para hexadecimal fica:\033[m {}'.format(num, hex(num)))
else:
    print('\033[36mOpção inválida tente novamente')