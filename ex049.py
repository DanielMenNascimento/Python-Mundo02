# Tabuada 2.0

n = int(input('Digite um número: '))
for c in range(1, 11):
    print('{:2} x {:>2} = {:<2}'.format(n, c, n * c))
