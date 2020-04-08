peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso/(altura**2)
print('Seu imc é de {:.1f}, seu status é:'.format(imc))
if imc<18.5:
    print('\033[36mabaixo do peso\033[m')
elif imc<=25:
    print('\33[32mpeso ideal\033[m')
elif imc<=30:
    print('\033[34msobrepeso\033[m')
elif imc<=40:
    print('\033[31mobesidade\033[m')
elif imc>40:
    print('\033[31mobesidade mórbida\033[m')