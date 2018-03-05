# Super Progressão Aritmética v3.0

print('-' * 30)
print('{:^30}'.format('Gerador de PA'))
print('-' * 30)

primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))

termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados!'.format(total))
