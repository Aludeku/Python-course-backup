reais=float(input('Quantos reais você tem? R$'))
dol=4.33
print('Com {:.2f} você possui US${:.2f}'.format(reais,reais/dol))
real=float(input('Quantos dólares você tem? US$'))
print('Neste caso você possui R${:.2f} reais'.format(real*dol))