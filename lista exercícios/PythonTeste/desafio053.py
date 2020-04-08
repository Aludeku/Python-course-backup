frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = juntar[::-1]
print ('o inverso de {} é {}. portanto'.format(juntar,inverso))
if juntar == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')