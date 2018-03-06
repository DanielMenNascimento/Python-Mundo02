# Tabuada V3.0
print('=' * 30)
print('{:^30}'.format('TABUADA'))
print('=' * 30)
while True:
    n = int(input('Digite um número:'))

    if n < 0:
        break

    for c in range(1, 11):
        print('{:<} x {:>2} = {:<}'.format(n, c, n * c))
    print('-' * 30)

print('FIM')
