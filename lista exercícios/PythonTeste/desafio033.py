a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
#verificando menor
menor = a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
#verificando maior
maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O menor número foi {}.'.format(menor))
print('O maior número foi {}.'.format(maior))