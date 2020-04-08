from time import sleep
from random import randint
print('\033[31;46m CONTAGEM REGRESSIVA \033[m')
for c in range(10,0,-1):
    sleep(1)
    r = randint(31, 37)
    print('\033[{}m {} \033[m'.format(r,c))
sleep(1)
print('\033[31m AU AU BOOM PTSS\033[m')