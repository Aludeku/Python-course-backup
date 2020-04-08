frase = str(input('Digite uma frase qualquer: ')).lower().strip()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra "a" da frase aparece na posição {}'.format(frase.find('a')+1))
print('A última letra "a" da frase aparece na posição {}'.format(frase.rfind('a')+1))