print('\033[36;45m TABUADA USELESS ALU \033[m')
n = int(input('\033[36mDigite um número inteiro: \033[m'))
for c in range(0,11):
    print('{} x {} = {}'.format(n,c,n*c))