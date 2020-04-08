from random import randint
print("\033[1;30;45mSUPER DESAFIO TENTE ACERTAR O NÚMERO QUE O BOT ESCOLHEU DE 17 À 89\033[m")
print('=-'*20)
number = randint(17,89)
escolher = int(input("Agora qual número você aposta que o bot burro escolheu? "))
if escolher == number:
    print("BAH MEU, VOCÊ ACERTOU!! O BOT ESTÚPIDO ESCOLHEU EXATAMENTE O NÚMERO {}".format(number))
else:
    print("Poisé meu amigo parece que essa é uma vitória das máquinas, o bot escolheu {}".format(number))
