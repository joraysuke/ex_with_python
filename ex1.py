# Cáculo do valor de Pi:

import random

n = int(input('Quantos pontos você deseja gerar: '))
circ = 0

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    #print(x,y)

    if (x*x + y*y)**(1/2) <= 1:
        circ += 1

pi = circ/n*4
print(pi)
