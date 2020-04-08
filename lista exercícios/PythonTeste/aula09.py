n1 = float(input('Qual foi sua nota na primeira prova?'))
n2 = float(input('Qual foi sua nota na segunda prova?'))
média = (n1+n2)/2
print('Sua média é {:.1f}'.format(média))
if média>=60<90:
    print('\033[0;32mSua nota é acima da média, parabéns')
if média<=60:
    print('\033[31mSua nota foi abaixo que o esperado, se esforce mais!')
if média>=90:
    print('Sua nota foi excelente, meus parabéns')
