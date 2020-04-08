print('Veja se é possível criar um triangulo dadas as retas: ')
reta1 = float(input('Primeira reta: '))
reta2 = float(input('Segunda reta: '))
reta3 = float(input('Terceira reta: '))
if reta1+reta2>reta3 and reta1+reta3>reta2 and reta2+reta3>reta1:
    print('É possível criar um triângulo ',end='')
    if reta1==reta2==reta3:
        print('\033[32mequilátero\033[m')
    elif reta1!=reta2!=reta3!=reta1:
        print('\033[34mescaleno\033[m')
    elif reta1==reta2!=reta3 or reta3==reta1!=reta2 or reta2==reta3!=reta1:
        print('\033[35misósceles\033[m')
else:
    print('Não é possível formar um triângulo!')