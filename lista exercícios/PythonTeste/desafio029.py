veloc = int(input('A que velocidade seu carro está andando? '))
if veloc>=81:
    print('poxa vida sua velocidade é de {}km/h porém o limite é de 80km/h, você foi multado!'.format(veloc))
else:
    print('Sua velocidade é de {}km/h, tudo nos trinks'.format(veloc))