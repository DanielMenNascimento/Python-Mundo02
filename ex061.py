# Progressão Aritmética v2.0

print('-' * 30)
print('{:^30}'.format('Gerador de PA'))
print('-' * 30)

n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = n
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += r
    cont += 1
print('FIM!!!')