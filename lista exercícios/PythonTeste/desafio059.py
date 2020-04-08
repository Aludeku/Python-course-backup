escolha = 0
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while escolha != 5:
    escolha = int(input('\033[5mAgora escolha\033[6m: \n[1] para somar;\n[2] para multiplicar; \n[3] para saber qual o maior; \n[4] para novos números;\n[5] para sair do programa:'))
    if escolha == 1:
        soma = n1 + n2
        print('\033[30;45m{} + {} = {}.\033[m'.format(n1,n2,soma))
    elif escolha == 2:
        multi = n1 * n2
        print('\033[30;45m{} X {} = {}.\033[m'.format(n1,n2,multi))
    elif escolha == 3:
        if n1 > n2:
            print('\033[30;45m{} > {}.\033[m'.format(n1,n2))
        else:
            print('\033[30;45m{} < {}.\033[m'.format(n1,n2))
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número novamente: '))
        n2 = int(input('Digite o segundo número novamente: '))
    sleep(2)
print('\033[92mMuito obrigado por usar o sistema, espero que tenha gostado! :)\033[m')