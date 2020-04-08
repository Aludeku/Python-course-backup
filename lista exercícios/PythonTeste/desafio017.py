from math import hypot
oposto = float(input('Qual o comprimento do cateto \033[35moposto\033[m? '))
adjacente = float(input('Qual o comprimento do cateto \033[35madjacente\033[m? '))
hipotenusa = hypot(oposto,adjacente)
print('a hipotenusa vai medir \033[36m{:.2f}'.format(hipotenusa))