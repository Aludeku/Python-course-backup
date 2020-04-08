resp = "Y"
sum = quant = average = bigger = smaller = 0
while resp in 'Yy':
    num = int(input('Say a number: '))
    sum += num
    quant += 1
    if quant == 1:
        bigger = smaller = num
    else:
        if num > bigger:
            bigger = num
        if num < smaller:
            smaller = num
    resp = str(input('Do you want to continue? [Y/N] ')).upper().strip()[0]
average = sum / quant
print('Você digitou {} números, a média entre os números digitados foi {}'.format(quant, average))
print('O maior é {} e o menor {}'.format(bigger, smaller))