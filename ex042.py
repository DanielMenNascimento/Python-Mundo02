# Analisando Triângulos v2.0

r1 = float(input('1° Segmento: '))
r2 = float(input('2° Segmento: '))
r3 = float(input('3° Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Os segmentos podem formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
        print('Pois tem todos os lados iguais.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
        print('Pois tem todos os lados diferentes.')
    else:
        print('ISÓSELES!')
        print('Pois tem dois lados iguais.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
