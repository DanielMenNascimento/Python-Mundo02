'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números
que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

contador = 0
quant = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        quant += 1
        contador += c
print('\nA soma dos {} valores foi {}'.format(quant, contador))
