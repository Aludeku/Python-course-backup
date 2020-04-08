n1 = 0
quantosn = 0
soma = 0
while n1 != 999:
    n1 = int(input('Digite um valor: '))
    quantosn += 1
    soma += n1
print('Foram digitados {} números e a soma entre eles é {}'.format((quantosn-1),soma-999))
print('Fim' )