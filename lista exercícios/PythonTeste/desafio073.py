times = ('Athletico', 'Fortaleza', 'Bragantino',
       'Palmeiras', 'Atlético-MG', 'Fluminense', 'Bahia',
       'Santos', 'Flamengo', 'Corinthians', 'Ceará',
       'Internacional', 'Juventude', 'Chapecoense')

print('-='*30)
print('Classificação Brasileirão')
print('-='*30)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-='*30)
print(f'Os últimos 4 colocados são {times[-4:]}')
print('-='*30)
print(f'Os times em ordem alfabética {sorted(times)}')
print('-='*30)
print(f'O chapecoense está na posição {times.index("Chapecoense")+1}')