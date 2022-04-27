data = {}
gols = []
data['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {data["nome"]} jogou? '))
for g in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {g+1}? ')))
data['gols'] = gols[:]
data['total'] = sum(gols)
print(data)
print('-='*20)
print(f'O campo nome tem o valor {data["nome"]}.')
print(f'O campo gols tem o valor {gols}.')
print(f'O campo total tem o valor {data["total"]}.')
print('-='*20)
print(f'O jogador {data["nome"]} jogou {partidas}.')
for c in range(0, partidas):
    print(f'    => Na partida {c+1}, fez {gols[c]} gols.')
    print(f'Foi um total de {data["total"]} gols!')