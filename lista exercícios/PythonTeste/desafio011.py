larg=float(input('Quantos metros tem a largura da parede?'))
alt=float(input('Quantos metros tem a altura da parede?'))
area=larg*alt
tint=area/2
print('A área dessa parede é {}m², será necessário {} litros de tinta para pintar essa parede'.format(area,tint))