# Detector de Palíndromo

from time import sleep
frase = str(input('Digite algo: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('{} | {}'.format(junto, inverso))
sleep(1)
print('ANALISANDO...')
sleep(1)
if inverso == junto:
    print('\033[1;32mÉ um palíndromo!\033[m')
else:
    print('\033[31mNão é um palíndromo!\033[m')
