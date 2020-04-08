number = int(input('Say a number: '))
u = number // 1 % 10
d = number // 10 % 10
h = number // 100 % 10
t = number // 1000 % 10
print('Analyzing number',number)
print('unit:{}'.format(u))
print('Dozen:{}'.format(d))
print('Hundreds:{}'.format(h))
print('Thousands:{}'.format(t))