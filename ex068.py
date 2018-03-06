# Par ou Impar

from random import randint

vitorias = 0
correto = ''

while True:

    jogador = int(input('Escolha um número: '))
    maquina = randint(1, 10)
    total = jogador + maquina
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]

    print('=' * 17)
    print('= Você ----> {:2} ='.format(jogador))
    print('= Máquina -> {:2} ='.format(maquina))
    print('-' * 17)
    print('= Total ---> {:2} ='.format(total))
    print('=' * 17)

    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break

print('-=' * 15)
print('Você venceu {} vezes.'.format(vitorias))
print('-=' * 15)
