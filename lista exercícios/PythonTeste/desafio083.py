expr = str(input('Digite uma expressão: '))
lista = []
for c in expr:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) > 0:
    print('Sua expressão está incorreta')
else:
    print('Sua expressão está correta')