# Análise completa
'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
 mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
medidade = 0
maioridade = 0
maisvelho = ''
totmulher20 = 0

for pessoa in range(1, 6):
    print('----------{}° Pessoa ----------'.format(pessoa))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    somaidade += idade
    medidade = somaidade / 5
    if pessoa == 1 and sexo in 'Mm':
        maioridade = idade
        maisvelho = nome

    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        maisvelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print('-' * 30)
print('A média de idade do grupo é de {:.1f} anos.'.format(medidade))
print('{} é o homem mais velho com seus bem vividos {} anos.'.format(maisvelho, maioridade))
print('Ao todo temos {} mulher(es) com menos de 20 anos.'.format(totmulher20))
