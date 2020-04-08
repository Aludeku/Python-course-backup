valor = float(input('\033[31mValor da casa:\033[m R$'))
salario = float(input('\033[32mSeu salário:\033[m R$'))
anos = int(input('\033[35mEm quantos anos pretende pagar?\033[m'))
prest = float(valor/(anos*12))
if prest >=0.30*salario:
    print("\033[31mA prestação excede 30% do seu salário, portanto o empréstimo será negado\033[m")
else: print('\033[36mVocê pagará prestações mensais de R${:.2f}\033[m'.format(prest))