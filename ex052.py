#  Números primos

total = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        total += 1
        print('\033[1;32m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
if total == 2:
    print('\n\033[mO número {} \033[1;32mÉ PRIMO\033[m'.format(n))
else:
    print('\n\033[mO número {} \033[1;31mNÃO É PRIMO\033[m'.format(n))
