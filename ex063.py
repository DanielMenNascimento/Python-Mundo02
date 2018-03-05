# Sequência de Fibonacci v1.0

print('=' * 45)
print('\033[1;30m{:^45}\033[m'.format('Sequência de Fibonacci'))
print('=' * 45)

n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-' * 45)
print('{} -> {}'.format(t1, t2), end=' -> ')
cont = 3
while cont <= n:
    t3 = t2 + t1
    print('{}'.format(t3), end=' -> ')
    cont += 1
    t1 = t2
    t2 = t3

print('FIM')
print('-' * 45)
