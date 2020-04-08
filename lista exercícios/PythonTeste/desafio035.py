print('-='*20)
print('Analisador de triângulos')
print('-='*20)
pri = int(input('veja se é possível formar um triangulo, diga a medida da primeira reta: '))
seg = int(input('A medida da segunda reta: '))
ter = int(input('a medida da terceira reta: '))
if pri+seg>ter and seg+ter>pri and ter+pri>seg:
    print('é possível formar um triângulo!')
else: print('Não é possível formar um triângulo!')