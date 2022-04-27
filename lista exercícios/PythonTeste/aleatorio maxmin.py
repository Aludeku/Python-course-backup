from random import randint
max = 0
min = 0
count = 0
while count != 5:
        rand: int = randint(0, 10)
        if rand >= max:
            max = rand
        elif rand <= min:
            min = rand
        count += 1
print(max)
print(min)