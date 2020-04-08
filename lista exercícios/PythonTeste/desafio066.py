num = sum = count = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
      break
    sum += num
    count += 1
print(f'você digitou {count} números a soma entre eles é {sum}')