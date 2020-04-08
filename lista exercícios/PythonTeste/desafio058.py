from random import randint
print('\033[31m-'*10,'O BOT MALUCO VAI PENSAR EM UM NÚMERO DE 1 À 10','-'*10)
bot = randint(1,10)
escolha = int(input('Dale, tenta adivinhar qual número o bot escolheu:'))
count = 1
while escolha != bot:
    count += 1
    if bot>escolha:
        print('\033[31m(Maior)\033[m')
    else:
        print('\033[32m(Menor)\033[m')
    escolha = int(input('Você errou meu, chuta outro:'))
if escolha == bot:
    if count>1:
        print('\033[mAí sim heim meu, demorou mas foi, o bot escolheu {}.'.format(bot))
        print('Houveram {} tentativas até o acerto'.format(count))
    elif count == 0:
        print('\033[32mWOW DE PRIMA, O bot escolheu {}.\033[m'.format(bot))
        print('Houveram {} tentativas até o acerto'.format(count))
