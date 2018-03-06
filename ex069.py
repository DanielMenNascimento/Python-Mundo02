# Análise de dados do grupo

cont = maior18 = homens = mulher20 = 0

while True:
    idade = int(input('Idade: '))

    if idade >= 18:
        maior18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

        if sexo == 'M':
            homens += 1

        if sexo == 'F':
            if idade >= 20:
                mulher20 += 1

    cont += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]

    print('-' * 30)

    if resp == 'N':
        break

print('Das {} pessoas cadastradas:'.format(cont))
print('{} tem mais que 18 anos'. format(maior18))
print('{} são homens.'.format(homens))
print('{} mulheres tem mais que 20 anos.'.format(mulher20))
