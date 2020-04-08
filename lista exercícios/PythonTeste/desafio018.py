from math import radians, cos, sin, tan
angulo = float(input('Digite o ângulo que você deseja ' ))
seno = sin(radians(angulo))
print('O ângulo {} tem o seno de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O ângulo {} tem o cosseno de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo {} tem a tangente de {:.2f}'.format(angulo,tangente))