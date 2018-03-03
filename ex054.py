# Grupo da Maioridade

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento da {}° pessoa: '.format(c)))
    if atual - ano >= 21:
        maior += 1
    else:
        menor += 1
print('Das {} datas consultadas, constatamos que:'.format(c))
print('Maior(es) de idade = {}'.format(maior))
print('Menor(es) de idade = {}'.format(menor))
