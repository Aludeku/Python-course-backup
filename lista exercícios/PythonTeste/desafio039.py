from datetime import date

atual = date.today().year
genero = str(input('Você é Homem ou Mulher? '))
if genero == 'Mulher':
    print('Você está dispensada Mulher!')

elif genero == 'Homem':
    nasc = int(input('Em que ano você nasceu? '))
age = atual - nasc

    if age<18:
        alist = 18 - age
    print('Falta(m) \033[31m{}\033[m ano(s) para você se alistar.'.format(alist))
    print('Você se alistará em ',alist+atual)
    elif: age == 18
    print('Você deve fazer seu alistamento este \033[31mano\033[m!')
    elif: age > 18
    alist = age - 18
    ano = atual - alist
    print('Já passou seu tempo de alistamento.')
    print('Você provavelmente se alistou em {}'.format(ano))