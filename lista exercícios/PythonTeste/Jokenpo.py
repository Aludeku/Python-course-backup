from random import randint
from time import sleep
escolha = int(input('''Escolha:
[0] para pedra
[1] para papel
[2] para tesoura: '''))
print('\033[35m  JO \033[m')
sleep(0.5)
print('\033[34m  KEN \033[m')
sleep(0.5)
print('\033[36m  PO \033[m')
sleep(0.5)
lista = ('pedra', 'papel', 'tesoura')
bot = randint(0,2)
if escolha>2:
    print('Opção inválida, burro')
else:
    print('Você escolheu {} e o computador escolheu {}'. format(lista[escolha],lista[bot]))

if escolha == 0 and bot == 0 or escolha == 1 and bot == 1 or escolha == 2 and bot ==2:
    print('Empate')
elif escolha == 0 and bot == 1 or escolha == 1 and bot == 2 or escolha == 2 and bot == 0:
    print('\033[31mVitória das máquinas\033[m')
elif escolha == 0 and bot == 2 or escolha == 1 and bot == 0 or escolha == 2 and bot == 1:
    print('\033[32mSim, vitória\033[m')
