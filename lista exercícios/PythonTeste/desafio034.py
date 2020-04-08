sal = float(input('De quanto é o seu salário? R$'))
if sal>=1250:
    au1 = (sal*0.10)+sal
    print('Você receberá um aumento de 10%, seu novo salário é de R${:.2f}'.format(au1))
else:
    au2 = (sal*0.15)+sal
    print('Você receberá um aumento de 15%, seu novo salário é de R${:.2f}'.format(au2))