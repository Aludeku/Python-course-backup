from datetime import date
nasc = int(input('em que ano você nasceu ?'))
atual = date.today().year
idade= int(atual - nasc)
if idade<=9:
    print('Sua categoria é a mirim')
elif idade<=14:
    print('Sua categoria é a infantil')
elif idade<=19:
    print('Sua categoria é a junior')
elif idade==20:
    print('sua categoria é a sênior')
else:
    print('Sua categoria é a MASTER')