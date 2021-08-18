from random import randint
from time import sleep
print('--'*15)
print('     JOGA NA MEGA SENA     ')
print('--'*15)
lista = []
jogos = []
questcount = 1
quest = int(input('Quantos sorteios você deseja? '))
print('=-'*3, f'Sorteando {quest} Jogos', '=-'*3)
while questcount <= quest:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    questcount += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)