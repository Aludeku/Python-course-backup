num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1>num2 :
    print('O número {} é maior que o número {}'.format(num1,num2))
elif num2>num1 :
    print('O número {} é maior que o número {}'.format(num2,num1))
else:
    print('Não existe valor maior, os dois são iguais')