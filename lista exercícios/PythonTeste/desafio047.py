print('\033[32;46m TODOS OS NÚMEROS PARES ATÉ O NÚMERO QUE VOCÊ QUISER \033[m')
n = int(input('\033[32mQual número você quer?\033[m'))
for c in range(1, n):
    if c % 2 == 0:
        print(c, end=' ')