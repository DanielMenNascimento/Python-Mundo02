# Estatísticas em produtos

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1

    if preco >= 1000:
        totmil += 1

    if cont == 1:
        menor = preco
        barato = produto

    if preco < menor:
        menor = preco
        barato = produto


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
    print('-' * 30)

print('{:-^30}'.format('={ FIM }='))
print('Total = R${:<.2f}'.format(total))
print('{} produtos custaram mais de R$1000,00'.format(totmil))
print('{} foi o produto mais barato custando apenas R${:.2f}'.format(barato, menor))
