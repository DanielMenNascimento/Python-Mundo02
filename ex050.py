# Soma dos pares

par = 0
impar = 0
soma = 0

for c in range(1, 7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        par += 1
        soma += n
    else:
        impar += 1
print('Dos {} números digitados, {} são pares e {} são impares.'.format(c, par, impar))
print('A soma dos números pares é {}'.format(soma))
