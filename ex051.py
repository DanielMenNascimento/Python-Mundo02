# Progressão Aritimética

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = n + (10 - 1) * r
for c in range(n, dec + r, r):
    print(c, end=' ')
