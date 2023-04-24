import random

x0=100

x=x0

banco = 0

vitorias = 0
for a in range(1000):
    while x >=0:
        for i in range(20):
            if random.randint(0,1):
                x+=1
            else:
                x-=1
        if x>x0:
            banco += x-x0
            x=x0

    print(banco)

if banco > x0:
    vitorias += 1

else:
    vitorias += -1

