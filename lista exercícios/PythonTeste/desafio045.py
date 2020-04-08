from random import randint
print('\033[30;45m  JOKENPO COM O BOT BURRO   \033[m')
print('~~'*30)
decida = int(input('\033[30;45m DECIDA: digite\033[m\033[30;41m 1 \033[m\033[30;45mpara pedra,\033[m\033[30;41m 2 \033[m\033[30;45mpara papel ou\033[30;41m 3 \033[m\033[30;45mpara tesoura:\033[m '))
bot = randint(1,3)
if decida==1 and bot ==1 or decida==2 and bot==2 or decida==3 and bot==3:
    print('Você escolheu {} e o bot também, portanto,\033[31mEMPATE BURRO\033[31m'.format(decida))
elif decida==1 and bot==2 or decida==2 and bot==3 or decida==3 and bot==1:
    print('Você escolheu {} e o bot {}, portanto, \033[31mVITÓRIA DAS MÁQUINAS\033[31m'.format(decida,bot))
else:
    print('Wow você venceu ok?')