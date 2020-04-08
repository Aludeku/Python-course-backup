compra = float(input('Qual o valor da compra? R$'))
opçao = int(input('De que forma você pretende pagar?\n[1] à vista\n[2]no cartão\n[3]2x no cartão\n[4]3x ou mais no cartão:'))
if opçao == 1:
    print('R${:.2f} à vista custará R${:.2f}'.format(compra,compra-(compra*0.10)))
elif opçao == 2:
    print('R${:.2f} à vista no cartão custará R${:.2f}'.format(compra,compra-(compra*0.05)))
elif opçao == 3:
    print('Sua compra de R${:.2f} será parcelada em duas vezes de R${:.2f}, R${:.2f} ao todo.'.format(compra,compra/2,compra))
elif opçao == 4:
    vezes = int(input('em quantas vezes?'))
    print('R${:.2f} em {} vezes de R${:.2f}, no cartão custará R${:.2f}'.format(compra,vezes,compra/vezes,compra+(compra*0.20)))
else:
    print('\033[31mOpção inválida\033[m')